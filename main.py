from antlr4 import *
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <source.cyx>")
        return
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = CyamixLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CyamixParser(stream)
    tree = parser.program()
    print("Parsing succeeded (no syntax errors).")
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()