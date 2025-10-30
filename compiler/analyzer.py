from antlr4 import *
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser
from code_generator import CyamixToCVisitor

class Analyzer:
    def __init__(self, code):
        self.code = code
        self.visitor = CyamixToCVisitor()

    def parse(self):
        input_stream = InputStream(self.code)
        lexer = CyamixLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CyamixParser(tokens)
        tree = parser.program()
        return tree

    def generate_c_code(self):
        tree = self.parse()
        self.visitor.visit(tree)
        return self.visitor.code
