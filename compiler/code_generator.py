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
        }.get(type_name, type_name)

        value = ""
        if ctx.expr():
            expr_value = self.visit(ctx.expr())
            value = f" = {expr_value}" if expr_value else ""

        line = f"{c_type} {name}{value};\n"
        return line

    # -------------------------
    # Assignments
    # -------------------------
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr()) or ""
        line = f"{name} = {value};\n"
        return line

    # -------------------------
    # Expressions
    # -------------------------
    def visitExpr(self, ctx):
        # expr -> logicalOrExpr
        return self.visit(ctx.getChild(0))

    def visitLogicalOrExpr(self, ctx):
        parts = [self.visit(ctx.logicalAndExpr(i)) for i in range(len(ctx.logicalAndExpr()))]
        return " || ".join(parts)

    def visitLogicalAndExpr(self, ctx):
        parts = [self.visit(ctx.equalityExpr(i)) for i in range(len(ctx.equalityExpr()))]
        return " && ".join(parts)

    def visitEqualityExpr(self, ctx):
        rel_exprs = list(ctx.relationalExpr())
        children = list(ctx.getChildren())
        expr = self.visit(rel_exprs[0])
        for i, rel in enumerate(rel_exprs[1:]):
            op = children[i*2 + 1].getText()  # operador entre os relationalExpr
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
    # Function Call
    # -------------------------
    def visitFuncCall(self, ctx):
        func_name = ctx.getChild(0).getText()
        args = ""
        if ctx.argList():
            arg_values = [self.visit(arg) for arg in ctx.argList().arg()]
            args = ", ".join(arg_values)
        line = f"{func_name}({args});\n"
        return line

    # -------------------------
    # Program
    # -------------------------
    def visitProgram(self, ctx):
        out = []
        # geralmente o último filho é EOF
        for i in range(ctx.getChildCount() - 1):
            res = self.visit(ctx.getChild(i))
            if isinstance(res, str):
                out.append(res)
        text = "".join(out)
        self.code = text  # único ponto onde populamos self.code
        return text

    # -------------------------
    # Top-level Declarations
    # -------------------------
    def visitTopDecl(self, ctx):
        # ajuste conforme sua gramática (se topDecl puder ser mais do que varDecl)
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        if ctx.statement():
            return self.visit(ctx.statement())
        return ""

    # -------------------------
    # Statements
    # -------------------------
    def visitStatement(self, ctx):
        for i in range(ctx.getChildCount()):
            res = self.visit(ctx.getChild(i))
            if isinstance(res, str) and res != "":
                return res
        return ""

    # -------------------------
    # Block
    # -------------------------
    def visitBlock(self, ctx):
        text = "{\n"
        for i in range(1, ctx.getChildCount() - 1):
            res = self.visit(ctx.getChild(i))
            if isinstance(res, str):
                text += res
        text += "}\n"
        return text

    # -------------------------
    # If / Else
    # -------------------------
    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        then_code = self.visit(ctx.statement(0))
        code = f"if ({cond}) {then_code}"
        if ctx.statement(1):
            code += f"else {self.visit(ctx.statement(1))}"
        return code

    # -------------------------
    # While
    # -------------------------
    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.statement())
        code = f"while ({cond}) {body}"
        return code

    # -------------------------
    # Do While
    # -------------------------
    def visitDoWhileStmt(self, ctx):
        body = self.visit(ctx.statement())
        cond = self.visit(ctx.expr())
        code = f"do {body} while ({cond});\n"
        return code

    # -------------------------
    # For Loop
    # -------------------------
    def visitForStmt(self, ctx):
        init = self.visit(ctx.forInit()) if ctx.forInit() else ""
        cond = self.visit(ctx.expr()) if ctx.expr() else ""
        update = self.visit(ctx.forUpdate()) if ctx.forUpdate() else ""
        body = self.visit(ctx.statement())
        init = init.strip()
        if init.endswith(";"):
            init = init[:-1]
        code = f"for ({init}; {cond}; {update}) {body}"
        return code

    # -------------------------
    # For Init
    # -------------------------
    def visitForInit(self, ctx):
        if ctx.varDeclNoSemi():
            return self.visit(ctx.varDeclNoSemi())
        if ctx.assignmentNoSemi():
            return self.visit(ctx.assignmentNoSemi())
        return ""

    # -------------------------
    # For Update
    # -------------------------
    def visitForUpdate(self, ctx):
        return ", ".join(self.visit(a) for a in ctx.assignmentNoSemi())

    # -------------------------
    # Assignment (no semicolon)
    # -------------------------
    def visitAssignmentNoSemi(self, ctx):
        return f"{ctx.ID().getText()} = {self.visit(ctx.expr())}"

    # -------------------------
    # Var Declaration (no semicolon)
    # -------------------------
    def visitVarDeclNoSemi(self, ctx):
        type_name = ctx.type_().getText()
        name = ctx.ID().getText()
        c_type = {
            "int": "int",
            "float": "float",
            "char": "char",
            "boolean": "int"
        }.get(type_name, type_name)
        init = ""
        if ctx.expr():
            init = f" = {self.visit(ctx.expr())}"
        return f"{c_type} {name}{init}"

    # -------------------------
    # Relational Expressions
    # -------------------------
    def visitRelationalExpr(self, ctx):
        adds = list(ctx.additiveExpr())
        children = list(ctx.getChildren())
        expr = self.visit(adds[0])
        for i, a in enumerate(adds[1:]):
            op = children[i*2 + 1].getText()
            expr = f"{expr} {op} {self.visit(a)}"
        return expr

    # -------------------------
    # Function Call Arguments
    # -------------------------
    def visitArgList(self, ctx):
        return ", ".join(self.visit(a) for a in ctx.arg())

    def visitArg(self, ctx):
        if ctx.expr():
            return self.visit(ctx.expr())
        for i in range(ctx.getChildCount() - 1):
            if ctx.getChild(i).getText() == "&":
                return f"&{ctx.getChild(i+1).getText()}"
        return ""
