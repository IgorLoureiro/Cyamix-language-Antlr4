# Generated from Cyamix.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CyamixParser import CyamixParser
else:
    from CyamixParser import CyamixParser

# This class defines a complete listener for a parse tree produced by CyamixParser.
class CyamixListener(ParseTreeListener):

    # Enter a parse tree produced by CyamixParser#program.
    def enterProgram(self, ctx:CyamixParser.ProgramContext):
        pass

    # Exit a parse tree produced by CyamixParser#program.
    def exitProgram(self, ctx:CyamixParser.ProgramContext):
        pass


    # Enter a parse tree produced by CyamixParser#topDecl.
    def enterTopDecl(self, ctx:CyamixParser.TopDeclContext):
        pass

    # Exit a parse tree produced by CyamixParser#topDecl.
    def exitTopDecl(self, ctx:CyamixParser.TopDeclContext):
        pass


    # Enter a parse tree produced by CyamixParser#varDecl.
    def enterVarDecl(self, ctx:CyamixParser.VarDeclContext):
        pass

    # Exit a parse tree produced by CyamixParser#varDecl.
    def exitVarDecl(self, ctx:CyamixParser.VarDeclContext):
        pass


    # Enter a parse tree produced by CyamixParser#varItem.
    def enterVarItem(self, ctx:CyamixParser.VarItemContext):
        pass

    # Exit a parse tree produced by CyamixParser#varItem.
    def exitVarItem(self, ctx:CyamixParser.VarItemContext):
        pass


    # Enter a parse tree produced by CyamixParser#statement.
    def enterStatement(self, ctx:CyamixParser.StatementContext):
        pass

    # Exit a parse tree produced by CyamixParser#statement.
    def exitStatement(self, ctx:CyamixParser.StatementContext):
        pass


    # Enter a parse tree produced by CyamixParser#block.
    def enterBlock(self, ctx:CyamixParser.BlockContext):
        pass

    # Exit a parse tree produced by CyamixParser#block.
    def exitBlock(self, ctx:CyamixParser.BlockContext):
        pass


    # Enter a parse tree produced by CyamixParser#ifStmt.
    def enterIfStmt(self, ctx:CyamixParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CyamixParser#ifStmt.
    def exitIfStmt(self, ctx:CyamixParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CyamixParser#whileStmt.
    def enterWhileStmt(self, ctx:CyamixParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by CyamixParser#whileStmt.
    def exitWhileStmt(self, ctx:CyamixParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by CyamixParser#doWhileStmt.
    def enterDoWhileStmt(self, ctx:CyamixParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by CyamixParser#doWhileStmt.
    def exitDoWhileStmt(self, ctx:CyamixParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by CyamixParser#forStmt.
    def enterForStmt(self, ctx:CyamixParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CyamixParser#forStmt.
    def exitForStmt(self, ctx:CyamixParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CyamixParser#forInit.
    def enterForInit(self, ctx:CyamixParser.ForInitContext):
        pass

    # Exit a parse tree produced by CyamixParser#forInit.
    def exitForInit(self, ctx:CyamixParser.ForInitContext):
        pass


    # Enter a parse tree produced by CyamixParser#forUpdate.
    def enterForUpdate(self, ctx:CyamixParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by CyamixParser#forUpdate.
    def exitForUpdate(self, ctx:CyamixParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by CyamixParser#assignment.
    def enterAssignment(self, ctx:CyamixParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CyamixParser#assignment.
    def exitAssignment(self, ctx:CyamixParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CyamixParser#assignmentNoSemi.
    def enterAssignmentNoSemi(self, ctx:CyamixParser.AssignmentNoSemiContext):
        pass

    # Exit a parse tree produced by CyamixParser#assignmentNoSemi.
    def exitAssignmentNoSemi(self, ctx:CyamixParser.AssignmentNoSemiContext):
        pass


    # Enter a parse tree produced by CyamixParser#varDeclNoSemi.
    def enterVarDeclNoSemi(self, ctx:CyamixParser.VarDeclNoSemiContext):
        pass

    # Exit a parse tree produced by CyamixParser#varDeclNoSemi.
    def exitVarDeclNoSemi(self, ctx:CyamixParser.VarDeclNoSemiContext):
        pass


    # Enter a parse tree produced by CyamixParser#funcCall.
    def enterFuncCall(self, ctx:CyamixParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CyamixParser#funcCall.
    def exitFuncCall(self, ctx:CyamixParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CyamixParser#argList.
    def enterArgList(self, ctx:CyamixParser.ArgListContext):
        pass

    # Exit a parse tree produced by CyamixParser#argList.
    def exitArgList(self, ctx:CyamixParser.ArgListContext):
        pass


    # Enter a parse tree produced by CyamixParser#arg.
    def enterArg(self, ctx:CyamixParser.ArgContext):
        pass

    # Exit a parse tree produced by CyamixParser#arg.
    def exitArg(self, ctx:CyamixParser.ArgContext):
        pass


    # Enter a parse tree produced by CyamixParser#expr.
    def enterExpr(self, ctx:CyamixParser.ExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#expr.
    def exitExpr(self, ctx:CyamixParser.ExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:CyamixParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:CyamixParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:CyamixParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:CyamixParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#equalityExpr.
    def enterEqualityExpr(self, ctx:CyamixParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#equalityExpr.
    def exitEqualityExpr(self, ctx:CyamixParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#relationalExpr.
    def enterRelationalExpr(self, ctx:CyamixParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#relationalExpr.
    def exitRelationalExpr(self, ctx:CyamixParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:CyamixParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:CyamixParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:CyamixParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:CyamixParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#unaryExpr.
    def enterUnaryExpr(self, ctx:CyamixParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by CyamixParser#unaryExpr.
    def exitUnaryExpr(self, ctx:CyamixParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by CyamixParser#primary.
    def enterPrimary(self, ctx:CyamixParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CyamixParser#primary.
    def exitPrimary(self, ctx:CyamixParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CyamixParser#type.
    def enterType(self, ctx:CyamixParser.TypeContext):
        pass

    # Exit a parse tree produced by CyamixParser#type.
    def exitType(self, ctx:CyamixParser.TypeContext):
        pass



del CyamixParser