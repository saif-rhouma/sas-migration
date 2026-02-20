from parser.generated.SASVisitor import SASVisitor
from ir.models import Program, DataStep, Merge, Set, Assignment, IfBlock, DoBlock, Expression


class IRVisitor(SASVisitor):

    def __init__(self, token_stream=None, comments=None):
        super().__init__()
        self.token_stream = token_stream
        self.comments = comments or []
        
    def visitParse(self, ctx):
        program = Program()
        program.comments = self.comments  # use pre-extracted comments

        for block in ctx.sas_stmt_block():
            step = self.visit(block)
            if step:
                program.steps.append(step)

        return program


    # -------------------------
    # DATA STEP
    # -------------------------

    def visitData_stmt_block(self, ctx):
        # DATA target
        target_token = ctx.Identifier() or ctx.ID_NULL()
        target_name = target_token.getText()
        data_step = DataStep(target=target_name)

        # Track LIBNAME statements inside the DATA step (or globally)
        for stmt_ctx in ctx.data_stmt_list():
            if hasattr(stmt_ctx, 'LIBNAME'):
                libname = stmt_ctx.LIBNAME().getText()
                data_step.dependencies.append(libname)

            # visit children normally
            result = self.visit(stmt_ctx)
            if result:
                if isinstance(result, list):
                    data_step.operations.extend(result)
                else:
                    data_step.operations.append(result)

        return data_step


    def visitSet_stmt(self, ctx):
        datasets = [n.getText() for n in ctx.name()]
        token_index = ctx.start.tokenIndex
        # register XLSX or SQL sources if dataset name matches LIBNAME
        return Set(dataset=datasets, token_index=token_index)

    def visitMerge_stmt(self, ctx):
        datasets = [n.getText() for n in ctx.name()]
        token_index = ctx.start.tokenIndex
        return Merge(datasets=datasets, token_index=token_index)

    def visitBy_stmt(self, ctx):
        by_cols = [n.getText() for n in ctx.name()]

        if hasattr(self, "_current_datastep"):
            for op in reversed(self._current_datastep.operations):
                if isinstance(op, Merge):
                    op.by = by_cols
                    break

        return None

    def visitAssignment_stmt(self, ctx):
        target = ctx.name().getText()
        expr = Expression(ctx.expression().getText())
        token_index = ctx.start.tokenIndex
        return Assignment(target=target, expr=expr, token_index=token_index)

    def visitIf_stmt(self, ctx):
        # Wrap condition in Expression object
        cond_expr = Expression(ctx.expression().getText())
        token_index = ctx.start.tokenIndex
        ifblock = IfBlock(condition=cond_expr, body=[], token_index=token_index)
        
      
        # THEN branch
        then_ctx = ctx.data_stmt_list(0)
        
        for stmt_ctx in then_ctx.children:
            res = self.visit(stmt_ctx)
            if res:
                if isinstance(res, list):
                    ifblock.body.extend(res)
                    
                else:
                    ifblock.body.append(res)
            
        # ELSE branch
        if len(ctx.data_stmt_list()) > 1:
            else_ctx = ctx.data_stmt_list(1)
            ifblock.else_body = []

            for stmt_ctx in else_ctx.children:
                res = self.visit(stmt_ctx)
                if res:
                    if isinstance(res, list):
                        ifblock.else_body.extend(res)
                    else:
                        ifblock.else_body.append(res)

        return ifblock

    def visitDo_block(self, ctx):
        do_block = DoBlock()
        for stmt_ctx in ctx.data_stmt_list():
            res = self.visit(stmt_ctx)
            if res:
                if isinstance(res, list):
                    do_block.statements.extend(res)
                else:
                    do_block.statements.append(res)
        return do_block

    # -------------------------
    # PROC
    # -------------------------

    def visitProc_stmt_block(self, ctx):
        proc_name = ctx.proc_name().getText().lower()
        dataset = None
        if ctx.proc_options():
            dataset = ctx.proc_options().name().getText()

        if proc_name == "means":
            variables = []
            for stmt in ctx.proc_stmt_list():
                if stmt.name():
                    variables = [n.getText() for n in stmt.name()]
            from ir.models import ProcMeans
            return ProcMeans(dataset=dataset, variables=variables)

        if proc_name == "freq":
            from ir.models import ProcFreq
            return ProcFreq(dataset=dataset)

        return None
