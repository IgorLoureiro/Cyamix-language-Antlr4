from CyamixVisitor import CyamixVisitor

class CyamixToCVisitor(CyamixVisitor):
    def __init__(self):
        self.code = ""

    # Example: variable declare
    def visitVarDecl(self, ctx):
        type = ctx.type().getText()
        name = ctx.ID().getText()
        c_type = {
            "int": "int",
            "float": "float",
            "char": "char",
            "boolean": "int"
        }[type]

        value = ""
        if ctx.expr():
            value = " = " + self.visit(ctx.expr())
        line = f"{c_type} {name}{value};\n"
        self.code += line
        return line

    # Example: Assignment
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        line = f"{name} = {value};\n"
        self.code += line
        return line

    # Example: full expression
    def visitIntLiteral(self, ctx):
        return ctx.getText()