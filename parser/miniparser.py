import re
from ir.models import DataStep, Operation, ProcStep

def parse_sas(sas_code: str):
    blocks = []

    # Parse DATA steps
    data_pattern = re.compile(
        r"data\s+(\w+(?:\.\w+)?);\s*set\s+(\w+(?:\.\w+)?);(?:\s*if\s+(.*?);)?\s*run;",
        re.IGNORECASE | re.DOTALL
    )
    for match in data_pattern.finditer(sas_code):
        target, source, condition = match.groups()
        ops = []
        if condition:
            ops.append(Operation(type="filter", condition=condition.strip()))
        blocks.append(DataStep(target=target, source=source, operations=ops))

    # Parse PROC MEANS
    means_pattern = re.compile(r"proc\s+means\s+data=(\w+(?:\.\w+)?);", re.IGNORECASE)
    for match in means_pattern.finditer(sas_code):
        blocks.append(ProcStep(type="proc_means", dataset=match.group(1)))

    return blocks