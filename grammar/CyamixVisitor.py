# Generated from Cyamix.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CyamixParser import CyamixParser
else:
    from CyamixParser import CyamixParser

# This class defines a complete generic visitor for a parse tree produced by CyamixParser.

class CyamixVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CyamixParser#program.
    def visitProgram(self, ctx:CyamixParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#topDecl.
    def visitTopDecl(self, ctx:CyamixParser.TopDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#varDecl.
    def visitVarDecl(self, ctx:CyamixParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#statement.
    def visitStatement(self, ctx:CyamixParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#block.
    def visitBlock(self, ctx:CyamixParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#ifStmt.
    def visitIfStmt(self, ctx:CyamixParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#whileStmt.
    def visitWhileStmt(self, ctx:CyamixParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:CyamixParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#forStmt.
    def visitForStmt(self, ctx:CyamixParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#forInit.
    def visitForInit(self, ctx:CyamixParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#forUpdate.
    def visitForUpdate(self, ctx:CyamixParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#assignment.
    def visitAssignment(self, ctx:CyamixParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#assignmentNoSemi.
    def visitAssignmentNoSemi(self, ctx:CyamixParser.AssignmentNoSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#varDeclNoSemi.
    def visitVarDeclNoSemi(self, ctx:CyamixParser.VarDeclNoSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#funcCall.
    def visitFuncCall(self, ctx:CyamixParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#argList.
    def visitArgList(self, ctx:CyamixParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#arg.
    def visitArg(self, ctx:CyamixParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#expr.
    def visitExpr(self, ctx:CyamixParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:CyamixParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:CyamixParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#equalityExpr.
    def visitEqualityExpr(self, ctx:CyamixParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#relationalExpr.
    def visitRelationalExpr(self, ctx:CyamixParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:CyamixParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:CyamixParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#unaryExpr.
    def visitUnaryExpr(self, ctx:CyamixParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#primary.
    def visitPrimary(self, ctx:CyamixParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CyamixParser#type.
    def visitType(self, ctx:CyamixParser.TypeContext):
        return self.visitChildren(ctx)



del CyamixParser