from ir.models import DataStep, Merge, Set, Assignment, IfBlock, DoBlock, ProcMeans, ProcFreq, Program
from typing import List

def compile_program(program: Program) -> str:
    code = ["import pandas as pd\n"]

    comments = sorted(program.comments, key=lambda c: c["token_index"])
    comment_index = 0

    for step in program.steps:

        # Collect all operations in order
        operations = getattr(step, "operations", [])

        for op in operations:

            # Inject comments BEFORE this operation
            while (
                comment_index < len(comments)
                and comments[comment_index]["token_index"] < op.token_index
            ):
                code.append("# " + comments[comment_index]["text"])
                comment_index += 1

            # Compile operation
            if isinstance(step, DataStep):
                code.extend(_compile_operation(step, op))

        # Blank line after step
        code.append("")

    # Remaining trailing comments
    while comment_index < len(comments):
        code.append("# " + comments[comment_index]["text"])
        comment_index += 1

    return "\n".join(code)


def _compile_datastep(step: DataStep) -> list[str]:
    lines = []

    # First, SET or MERGE
    for op in step.operations:
        if isinstance(op, Set):
            lines.append(f"{step.target} = {op.dataset}.copy()")
        elif isinstance(op, Merge):
            if op.by:
                lines.append(
                    f"{step.target} = pd.merge({op.datasets[0]}, {op.datasets[1]}, on={op.by})"
                )
            else:
                lines.append(
                    f"{step.target} = pd.merge({op.datasets[0]}, {op.datasets[1]})"
                )

    # Then assignments and IF blocks
    for op in step.operations:
        if isinstance(op, Assignment):
            lines.append(f"{step.target}['{op.target}'] = {op.expr.expr}")
        elif isinstance(op, IfBlock):
            lines.extend(_compile_ifblock(step.target, op))

    lines.append("")
    return lines



def _compile_ifblock(df_name: str, ifblock: IfBlock) -> list[str]:
    lines = []
    cond = ifblock.condition.expr

    for stmt in ifblock.body:

        if isinstance(stmt, Assignment):
            lines.append(
                f"{df_name}.loc[{df_name}['{cond}'], '{stmt.target}'] = {stmt.expr.expr}"
            )

        elif isinstance(stmt, DoBlock):  # 🔥 ADD THIS
            for inner in stmt.statements:
                if isinstance(inner, Assignment):
                    lines.append(
                        f"{df_name}.loc[{df_name}['{cond}'], '{inner.target}'] = {inner.expr.expr}"
                    )

        elif isinstance(stmt, IfBlock):
            lines.extend(_compile_ifblock(df_name, stmt))

    return lines

# def _compile_doblock(df_name: str, do_block: DoBlock) -> List[str]:
#     lines = []
#     for stmt in do_block.statements:
#         if isinstance(stmt, Assignment):
#             lines.append(f"{df_name}['{stmt.target}'] = {stmt.expr.expr}")
#         elif isinstance(stmt, IfBlock):
#             lines.extend(_compile_ifblock(df_name, stmt))
#     return lines

def _compile_operation(step: DataStep, op):
    lines = []

    if isinstance(op, Set):
        lines.append(f"{step.target} = {op.dataset}.copy()")

    elif isinstance(op, Merge):
        if op.by:
            lines.append(
                f"{step.target} = pd.merge({op.datasets[0]}, {op.datasets[1]}, on={op.by})"
            )
        else:
            lines.append(
                f"{step.target} = pd.merge({op.datasets[0]}, {op.datasets[1]})"
            )

    elif isinstance(op, Assignment):
        lines.append(f"{step.target}['{op.target}'] = {op.expr.expr}")

    elif isinstance(op, IfBlock):
        lines.extend(_compile_ifblock(step.target, op))

    return lines