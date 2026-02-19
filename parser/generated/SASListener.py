# Generated from parser/SAS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SASParser import SASParser
else:
    from SASParser import SASParser

# This class defines a complete listener for a parse tree produced by SASParser.
class SASListener(ParseTreeListener):

    # Enter a parse tree produced by SASParser#parse.
    def enterParse(self, ctx:SASParser.ParseContext):
        pass

    # Exit a parse tree produced by SASParser#parse.
    def exitParse(self, ctx:SASParser.ParseContext):
        pass


    # Enter a parse tree produced by SASParser#sas_stmt_block.
    def enterSas_stmt_block(self, ctx:SASParser.Sas_stmt_blockContext):
        pass

    # Exit a parse tree produced by SASParser#sas_stmt_block.
    def exitSas_stmt_block(self, ctx:SASParser.Sas_stmt_blockContext):
        pass


    # Enter a parse tree produced by SASParser#data_stmt_block.
    def enterData_stmt_block(self, ctx:SASParser.Data_stmt_blockContext):
        pass

    # Exit a parse tree produced by SASParser#data_stmt_block.
    def exitData_stmt_block(self, ctx:SASParser.Data_stmt_blockContext):
        pass


    # Enter a parse tree produced by SASParser#libname_stmt.
    def enterLibname_stmt(self, ctx:SASParser.Libname_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#libname_stmt.
    def exitLibname_stmt(self, ctx:SASParser.Libname_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#data_stmt_list.
    def enterData_stmt_list(self, ctx:SASParser.Data_stmt_listContext):
        pass

    # Exit a parse tree produced by SASParser#data_stmt_list.
    def exitData_stmt_list(self, ctx:SASParser.Data_stmt_listContext):
        pass


    # Enter a parse tree produced by SASParser#comment_stmt.
    def enterComment_stmt(self, ctx:SASParser.Comment_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#comment_stmt.
    def exitComment_stmt(self, ctx:SASParser.Comment_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#rename_stmt.
    def enterRename_stmt(self, ctx:SASParser.Rename_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#rename_stmt.
    def exitRename_stmt(self, ctx:SASParser.Rename_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#infile_stmt.
    def enterInfile_stmt(self, ctx:SASParser.Infile_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#infile_stmt.
    def exitInfile_stmt(self, ctx:SASParser.Infile_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#file_specification.
    def enterFile_specification(self, ctx:SASParser.File_specificationContext):
        pass

    # Exit a parse tree produced by SASParser#file_specification.
    def exitFile_specification(self, ctx:SASParser.File_specificationContext):
        pass


    # Enter a parse tree produced by SASParser#infile_options.
    def enterInfile_options(self, ctx:SASParser.Infile_optionsContext):
        pass

    # Exit a parse tree produced by SASParser#infile_options.
    def exitInfile_options(self, ctx:SASParser.Infile_optionsContext):
        pass


    # Enter a parse tree produced by SASParser#input_stmt.
    def enterInput_stmt(self, ctx:SASParser.Input_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#input_stmt.
    def exitInput_stmt(self, ctx:SASParser.Input_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#set_stmt.
    def enterSet_stmt(self, ctx:SASParser.Set_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#set_stmt.
    def exitSet_stmt(self, ctx:SASParser.Set_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#condition.
    def enterCondition(self, ctx:SASParser.ConditionContext):
        pass

    # Exit a parse tree produced by SASParser#condition.
    def exitCondition(self, ctx:SASParser.ConditionContext):
        pass


    # Enter a parse tree produced by SASParser#value.
    def enterValue(self, ctx:SASParser.ValueContext):
        pass

    # Exit a parse tree produced by SASParser#value.
    def exitValue(self, ctx:SASParser.ValueContext):
        pass


    # Enter a parse tree produced by SASParser#merge_stmt.
    def enterMerge_stmt(self, ctx:SASParser.Merge_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#merge_stmt.
    def exitMerge_stmt(self, ctx:SASParser.Merge_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#by_stmt.
    def enterBy_stmt(self, ctx:SASParser.By_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#by_stmt.
    def exitBy_stmt(self, ctx:SASParser.By_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:SASParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:SASParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#delete_stmt.
    def enterDelete_stmt(self, ctx:SASParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#delete_stmt.
    def exitDelete_stmt(self, ctx:SASParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#if_stmt.
    def enterIf_stmt(self, ctx:SASParser.If_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#if_stmt.
    def exitIf_stmt(self, ctx:SASParser.If_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#do_block.
    def enterDo_block(self, ctx:SASParser.Do_blockContext):
        pass

    # Exit a parse tree produced by SASParser#do_block.
    def exitDo_block(self, ctx:SASParser.Do_blockContext):
        pass


    # Enter a parse tree produced by SASParser#proc_stmt_block.
    def enterProc_stmt_block(self, ctx:SASParser.Proc_stmt_blockContext):
        pass

    # Exit a parse tree produced by SASParser#proc_stmt_block.
    def exitProc_stmt_block(self, ctx:SASParser.Proc_stmt_blockContext):
        pass


    # Enter a parse tree produced by SASParser#proc_name.
    def enterProc_name(self, ctx:SASParser.Proc_nameContext):
        pass

    # Exit a parse tree produced by SASParser#proc_name.
    def exitProc_name(self, ctx:SASParser.Proc_nameContext):
        pass


    # Enter a parse tree produced by SASParser#proc_options.
    def enterProc_options(self, ctx:SASParser.Proc_optionsContext):
        pass

    # Exit a parse tree produced by SASParser#proc_options.
    def exitProc_options(self, ctx:SASParser.Proc_optionsContext):
        pass


    # Enter a parse tree produced by SASParser#proc_stmt_list.
    def enterProc_stmt_list(self, ctx:SASParser.Proc_stmt_listContext):
        pass

    # Exit a parse tree produced by SASParser#proc_stmt_list.
    def exitProc_stmt_list(self, ctx:SASParser.Proc_stmt_listContext):
        pass


    # Enter a parse tree produced by SASParser#var_stmt.
    def enterVar_stmt(self, ctx:SASParser.Var_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#var_stmt.
    def exitVar_stmt(self, ctx:SASParser.Var_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#title_stmt.
    def enterTitle_stmt(self, ctx:SASParser.Title_stmtContext):
        pass

    # Exit a parse tree produced by SASParser#title_stmt.
    def exitTitle_stmt(self, ctx:SASParser.Title_stmtContext):
        pass


    # Enter a parse tree produced by SASParser#expression.
    def enterExpression(self, ctx:SASParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SASParser#expression.
    def exitExpression(self, ctx:SASParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SASParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SASParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SASParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SASParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SASParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SASParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SASParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SASParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SASParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SASParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SASParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SASParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SASParser#atom.
    def enterAtom(self, ctx:SASParser.AtomContext):
        pass

    # Exit a parse tree produced by SASParser#atom.
    def exitAtom(self, ctx:SASParser.AtomContext):
        pass


    # Enter a parse tree produced by SASParser#comparator.
    def enterComparator(self, ctx:SASParser.ComparatorContext):
        pass

    # Exit a parse tree produced by SASParser#comparator.
    def exitComparator(self, ctx:SASParser.ComparatorContext):
        pass


    # Enter a parse tree produced by SASParser#macro_definition.
    def enterMacro_definition(self, ctx:SASParser.Macro_definitionContext):
        pass

    # Exit a parse tree produced by SASParser#macro_definition.
    def exitMacro_definition(self, ctx:SASParser.Macro_definitionContext):
        pass


    # Enter a parse tree produced by SASParser#macro_call.
    def enterMacro_call(self, ctx:SASParser.Macro_callContext):
        pass

    # Exit a parse tree produced by SASParser#macro_call.
    def exitMacro_call(self, ctx:SASParser.Macro_callContext):
        pass


    # Enter a parse tree produced by SASParser#macro_body.
    def enterMacro_body(self, ctx:SASParser.Macro_bodyContext):
        pass

    # Exit a parse tree produced by SASParser#macro_body.
    def exitMacro_body(self, ctx:SASParser.Macro_bodyContext):
        pass


    # Enter a parse tree produced by SASParser#parameter_list.
    def enterParameter_list(self, ctx:SASParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by SASParser#parameter_list.
    def exitParameter_list(self, ctx:SASParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by SASParser#argument_list.
    def enterArgument_list(self, ctx:SASParser.Argument_listContext):
        pass

    # Exit a parse tree produced by SASParser#argument_list.
    def exitArgument_list(self, ctx:SASParser.Argument_listContext):
        pass


    # Enter a parse tree produced by SASParser#name.
    def enterName(self, ctx:SASParser.NameContext):
        pass

    # Exit a parse tree produced by SASParser#name.
    def exitName(self, ctx:SASParser.NameContext):
        pass



del SASParser