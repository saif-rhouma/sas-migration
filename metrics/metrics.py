import re
from collections import defaultdict

def count_total_codes(program):
    """
    Count top-level DATA / PROC blocks
    """
    return len(program.steps)


def count_total_lines(sas_code):
    """
    Count total non-empty lines
    """
    return len([l for l in sas_code.splitlines() if l.strip()])


def count_egps(program):
    """
    Count executable operations inside DATA steps
    + count each PROC as 1 execution group
    """
    total = 0

    for step in program.steps:

        # Count DATA step operations
        if hasattr(step, "operations"):
            total += len(step.operations)

        # Count PROC steps as 1
        if step.__class__.__name__.startswith("Proc"):
            total += 1

    return total


def compute_avg_complexity(program):
    """
    Simple cyclomatic-style complexity
    Base 1 per block + 1 per IF / DO / MERGE
    """
    total_complexity = 0
    block_count = 0

    for step in program.steps:
        complexity = 1  # base complexity

        if hasattr(step, "operations"):
            for op in step.operations:
                if op.__class__.__name__ in ["IfBlock", "DoBlock", "Merge"]:
                    complexity += 1

        total_complexity += complexity
        block_count += 1

    if block_count == 0:
        return 0

    return round(total_complexity / block_count, 2)


def compute_block_complexity(step):
    """
    Compute complexity score for a single DATA/PROC block
    Base 1 + decision points
    """
    complexity = 1

    if hasattr(step, "operations"):
        for op in step.operations:
            if op.__class__.__name__ in ["IfBlock", "DoBlock"]:
                complexity += 2
            elif op.__class__.__name__ == "Merge":
                complexity += 3

    return complexity


def classify_complexity(score):
    """
    Convert numeric score to level
    """
    if score <= 2:
        return "Low"
    elif score <= 5:
        return "Medium"
    else:
        return "High"


def compute_complexity_metrics(program):
    """
    Returns:
    - average complexity level
    - per block complexity
    - number of codes by level
    """

    if not program.steps:
        return {
            "average_complexity": "Low",
            "code_complexity": [],
            "distribution": {
                "Low": 0,
                "Medium": 0,
                "High": 0
            }
        }

    block_results = []
    total_score = 0

    distribution = {
        "Low": 0,
        "Medium": 0,
        "High": 0
    }

    for idx, step in enumerate(program.steps):
        score = compute_block_complexity(step)
        level = classify_complexity(score)

        block_results.append({
            "code_index": idx + 1,
            "score": score,
            "level": level
        })

        total_score += score
        distribution[level] += 1

    avg_score = total_score / len(program.steps)
    avg_level = classify_complexity(avg_score)

    return {
        "average_complexity": avg_level,
        "code_complexity": block_results,
        "distribution": distribution
    }

def count_data_tables(program):
    """
    Count unique dataset names from:
    - DATA statements
    - SET
    - MERGE
    - PROC DATA=
    """
    tables = set()

    for step in program.steps:

        # DATA table
        if hasattr(step, "name"):
            tables.add(step.name)

        # Operations inside DATA
        if hasattr(step, "operations"):
            for op in step.operations:

                if op.__class__.__name__ in ["Set", "Merge"]:
                    if hasattr(op, "tables"):
                        for t in op.tables:
                            tables.add(t)

        # PROC DATA=
        if hasattr(step, "data"):
            tables.add(step.data)

    return len(tables)


def count_hardcoded_paths(sas_code):
    """
    Count hardcoded file paths inside string literals
    """
    strings = re.findall(r'"([^"]+)"', sas_code)

    hcp_count = 0

    for s in strings:
        if (
            "\\" in s
            or "/" in s
            or s.lower().endswith((".csv", ".txt", ".xlsx", ".dat"))
        ):
            hcp_count += 1

    return hcp_count

def classify_dependency(name):
    """
    Classify dataset/file by extension or structure
    """

    lower = name.lower()

    if lower.endswith(".sas7bdat"):
        return "sas7bdat"
    elif lower.endswith(".csv"):
        return "csv"
    elif lower.endswith(".xlsx"):
        return "xlsx"
    elif lower.startswith("lib.") or "." in name:
        return "libname"
    elif "select" in lower or "from" in lower:
        return "sql"
    else:
        return "other"


def extract_string_literals(sas_code):
    return re.findall(r'"([^"]+)"', sas_code)


# def classify_dependency(name):
#     lower = name.lower()

#     if lower.endswith(".sas7bdat"):
#         return "sas7bdat"
#     elif lower.endswith(".csv"):
#         return "csv"
#     elif lower.endswith(".xlsx"):
#         return "xlsx"
#     elif lower.startswith("lib.") or "." in name:
#         return "libname"
#     elif "select" in lower or "from" in lower:
#         return "sql"
#     else:
#         return "other"


def analyze_data_dependencies(program, sas_code):
    # Predefine all categories
    dependency_counts = {
        "sas7bdat": 0,
        "libname": 0,
        "csv": 0,
        "xlsx": 0,
        "sql": 0,
        "other": 0,
        "hcp_per_table": 0
    }

    # Helper to classify a table name or path
    def classify_dependency(name: str):
        name_upper = name.upper()
        if ".SAS7BDAT" in name_upper:
            return "sas7bdat"
        elif ".CSV" in name_upper:
            return "csv"
        elif ".XLSX" in name_upper:
            return "xlsx"
        elif name_upper.startswith("LIBNAME"):
            return "libname"
        elif "SQL" in name_upper:
            return "sql"
        else:
            return "other"

    # -------- IR Dependencies --------
    for step in program.steps:

        # Detect LIBNAME or DATA table dependencies
        if hasattr(step, "name"):
            dep_type = classify_dependency(step.name)
            dependency_counts[dep_type] += 1

        # Operations inside DATA step
        if hasattr(step, "operations"):
            for op in step.operations:

                # LIBNAME detection inside expression
                if hasattr(op, "expr") and "LIBNAME" in op.expr.expr.upper():
                    dependency_counts["libname"] += 1
                    if "XLSX" in op.expr.expr.upper():
                        dependency_counts["xlsx"] += 1

                # CSV or HCP detection inside PUT / FILE statements
                if hasattr(op, "expr") and (".CSV" in op.expr.expr.upper()):
                    dependency_counts["csv"] += 1

                # Tables referenced inside operations
                if hasattr(op, "tables"):
                    for t in op.tables:
                        dep_type = classify_dependency(t)
                        dependency_counts[dep_type] += 1

        # PROC SQL detection
        if hasattr(step, "proc_name") and step.proc_name.upper() == "SQL":
            dependency_counts["sql"] += 1

        # DATA= option in PROC
        if hasattr(step, "data"):
            dep_type = classify_dependency(step.data)
            dependency_counts[dep_type] += 1

    # -------- Hardcoded Path Detection (HCP) --------
    # Count all string literals that contain / or \ as HCP
    string_literals = re.findall(r'"([^"]+)"', sas_code)
    hcp_count = sum(1 for s in string_literals if "/" in s or "\\" in s)
    dependency_counts["hcp_per_table"] = hcp_count

    # Ensure all categories are present even if 0
    for k in ["sas7bdat", "libname", "csv", "xlsx", "sql", "other", "hcp_per_table"]:
        dependency_counts.setdefault(k, 0)

    return dependency_counts