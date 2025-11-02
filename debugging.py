import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser
from compiler.utils import write_code_to_c_file
from compiler.code_generator import CyamixToCVisitor

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Error on {line}:{column} -> {msg}"
        self.errors.append(error_msg)

    def hasErrors(self):
        return len(self.errors) > 0

def main():
    cyx_file = 'tests/test.cyx'

    input_stream = FileStream(cyx_file, encoding='utf-8')
    
    lexer = CyamixLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CyamixParser(stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    print(f"Start parsing if {cyx_file}...")
    tree = parser.program()

    if error_listener.hasErrors():
        print("\nParsing faild! Errors found:")
        for error in error_listener.errors:
            print(error)
    else:
        print("\nParsing completed!")

        visitor = CyamixToCVisitor()
        visitor.visit(tree)
        c_code = visitor.code


        file_base_name = cyx_file.split('.cyx')[0]
        write_code_to_c_file(c_code, file_base_name)

        print("\nGenerated code in /generated/" + file_base_name + ".c")

if __name__ == "__main__":
    main()