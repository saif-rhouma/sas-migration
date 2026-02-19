# Generated from parser/SAS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SASParser import SASParser
else:
    from SASParser import SASParser

# This class defines a complete generic visitor for a parse tree produced by SASParser.

class SASVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SASParser#parse.
    def visitParse(self, ctx:SASParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#sas_stmt_block.
    def visitSas_stmt_block(self, ctx:SASParser.Sas_stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#data_stmt_block.
    def visitData_stmt_block(self, ctx:SASParser.Data_stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#libname_stmt.
    def visitLibname_stmt(self, ctx:SASParser.Libname_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#data_stmt_list.
    def visitData_stmt_list(self, ctx:SASParser.Data_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#comment_stmt.
    def visitComment_stmt(self, ctx:SASParser.Comment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#rename_stmt.
    def visitRename_stmt(self, ctx:SASParser.Rename_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#infile_stmt.
    def visitInfile_stmt(self, ctx:SASParser.Infile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#file_specification.
    def visitFile_specification(self, ctx:SASParser.File_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#infile_options.
    def visitInfile_options(self, ctx:SASParser.Infile_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#input_stmt.
    def visitInput_stmt(self, ctx:SASParser.Input_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#set_stmt.
    def visitSet_stmt(self, ctx:SASParser.Set_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#condition.
    def visitCondition(self, ctx:SASParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#value.
    def visitValue(self, ctx:SASParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#merge_stmt.
    def visitMerge_stmt(self, ctx:SASParser.Merge_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#by_stmt.
    def visitBy_stmt(self, ctx:SASParser.By_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:SASParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#delete_stmt.
    def visitDelete_stmt(self, ctx:SASParser.Delete_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#if_stmt.
    def visitIf_stmt(self, ctx:SASParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#do_block.
    def visitDo_block(self, ctx:SASParser.Do_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#proc_stmt_block.
    def visitProc_stmt_block(self, ctx:SASParser.Proc_stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#proc_name.
    def visitProc_name(self, ctx:SASParser.Proc_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#proc_options.
    def visitProc_options(self, ctx:SASParser.Proc_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#proc_stmt_list.
    def visitProc_stmt_list(self, ctx:SASParser.Proc_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#var_stmt.
    def visitVar_stmt(self, ctx:SASParser.Var_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#title_stmt.
    def visitTitle_stmt(self, ctx:SASParser.Title_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#expression.
    def visitExpression(self, ctx:SASParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#relationalExpression.
    def visitRelationalExpression(self, ctx:SASParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SASParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SASParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#atom.
    def visitAtom(self, ctx:SASParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#comparator.
    def visitComparator(self, ctx:SASParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#macro_definition.
    def visitMacro_definition(self, ctx:SASParser.Macro_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#macro_call.
    def visitMacro_call(self, ctx:SASParser.Macro_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#macro_body.
    def visitMacro_body(self, ctx:SASParser.Macro_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#parameter_list.
    def visitParameter_list(self, ctx:SASParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#argument_list.
    def visitArgument_list(self, ctx:SASParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#name.
    def visitName(self, ctx:SASParser.NameContext):
        return self.visitChildren(ctx)



del SASParser