from CyamixVisitor import CyamixVisitor

class CyamixToCVisitor(CyamixVisitor):
    def __init__(self):
        self.code = ""

    # Exemplo: variável declarada
    def visitVarDecl(self, ctx):
        tipo = ctx.type().getText()
        nome = ctx.ID().getText()
        c_tipo = {
            "int": "int",
            "float": "float",
            "char": "char",
            "boolean": "int"
        }[tipo]

        valor = ""
        if ctx.expr():
            valor = " = " + self.visit(ctx.expr())
        linha = f"{c_tipo} {nome}{valor};\n"
        self.code += linha
        return linha

    # Exemplo: atribuição
    def visitAssignment(self, ctx):
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        linha = f"{nome} = {valor};\n"
        self.code += linha
        return linha

    # Exemplo: expressão inteira
    def visitIntLiteral(self, ctx):
        return ctx.getText()