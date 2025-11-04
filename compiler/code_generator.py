from antlr4 import CommonTokenStream, InputStream
from grammar.CyamixLexer import CyamixLexer
from grammar.CyamixParser import CyamixParser
from grammar.CyamixVisitor import CyamixVisitor


class CyamixToCVisitor(CyamixVisitor):
    def __init__(self):
        self.code = ""

    # -------------------------
    # Declarations
    # -------------------------
    def visitVarDecl(self, ctx):
        type_name = ctx.type_().getText() 
        name = ctx.ID().getText()

        c_type = {
            "int": "int",
            "float": "float",
            "char": "char",
            "boolean": "int"  # boolean -> int
        }[type_name]

        value = ""
        if ctx.expr():
            expr_value = self.visit(ctx.expr())
            value = f" = {expr_value}" if expr_value else ""

        line = f"{c_type} {name}{value};\n"
        self.code += line
        return line

    # -------------------------
    # Assignments
    # -------------------------
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr()) or ""
        line = f"{name} = {value};\n"
        self.code += line
        return line

    # -------------------------
    # Expressions
    # -------------------------
    def visitExpr(self, ctx):
        return self.visit(ctx.getChild(0))  # expr -> logicalOrExpr

    def visitLogicalOrExpr(self, ctx):
        parts = [self.visit(ctx.logicalAndExpr(i)) for i in range(len(ctx.logicalAndExpr()))]
        return " || ".join(parts)

    def visitLogicalAndExpr(self, ctx):
        parts = [self.visit(ctx.equalityExpr(i)) for i in range(len(ctx.equalityExpr()))]
        return " && ".join(parts)

    def visitEqualityExpr(self, ctx):
        children = list(ctx.getChildren())
        if len(children) == 1:
            return self.visit(ctx.relationalExpr(0))
        expr = self.visit(ctx.relationalExpr(0))
        for i, op in enumerate(ctx.getChildren()[1::2]):
            right = self.visit(ctx.relationalExpr(i + 1))
            expr = f"{expr} {op.getText()} {right}"
        return expr

    def visitEqualityExpr(self, ctx):
        rel_exprs = list(ctx.relationalExpr())  # todos os relationalExpr filhos
        children = list(ctx.getChildren())      # todos os filhos (expressões e operadores)
        
        expr = self.visit(rel_exprs[0])
        # operadores estão entre os relationalExpr, começando no índice 1 e pulando de 2 em 2
        for i, rel in enumerate(rel_exprs[1:]):
            op = children[i*2 + 1].getText()  # pega operador
            expr = f"{expr} {op} {self.visit(rel)}"
        return expr

    def visitAdditiveExpr(self, ctx):
        children = list(ctx.getChildren())
        if len(children) == 1:
            return self.visit(ctx.multiplicativeExpr(0))
        expr = self.visit(ctx.multiplicativeExpr(0))
        for i, op in enumerate(ctx.getChildren()[1::2]):
            right = self.visit(ctx.multiplicativeExpr(i + 1))
            expr = f"{expr} {op.getText()} {right}"
        return expr

    def visitMultiplicativeExpr(self, ctx):
        children = list(ctx.getChildren())
        if len(children) == 1:
            return self.visit(ctx.unaryExpr(0))
        expr = self.visit(ctx.unaryExpr(0))
        for i, op in enumerate(ctx.getChildren()[1::2]):
            right = self.visit(ctx.unaryExpr(i + 1))
            expr = f"{expr} {op.getText()} {right}"
        return expr

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.getChild(1))
            return f"{op}{val}"
        else:
            return self.visit(ctx.getChild(0))

    # -------------------------
    # Primary: literals, identifiers, parentheses
    # -------------------------
    def visitPrimary(self, ctx):
        if ctx.INT_LITERAL():
            return ctx.INT_LITERAL().getText()
        if ctx.FLOAT_LITERAL():
            return ctx.FLOAT_LITERAL().getText()
        if ctx.CHAR_LITERAL():
            return ctx.CHAR_LITERAL().getText()
        if ctx.BOOL_LITERAL():
            return ctx.BOOL_LITERAL().getText()
        if ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.expr():
            return f"({self.visit(ctx.expr())})"
        return ""

    # -------------------------
    # Optional: print statements
    # -------------------------
    def visitFuncCall(self, ctx):
        func_name = ctx.getChild(0).getText()
        args = ""
        if ctx.argList():
            arg_values = [self.visit(arg) for arg in ctx.argList().arg()]
            args = ", ".join(arg_values)
        line = f"{func_name}({args});\n"
        self.code += line
        return line
