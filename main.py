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
        error_msg = f"Erro na Linha {line}:{column} -> {msg}"
        self.errors.append(error_msg)

    def hasErrors(self):
        return len(self.errors) > 0

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <source.cyx>")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    
    lexer = CyamixLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CyamixParser(stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    print(f"Iniciando parsing de {sys.argv[1]}...")
    tree = parser.program()

    if error_listener.hasErrors():
        print("\nParsing falhou! Erros encontrados:")
        for error in error_listener.errors:
            print(error)
    else:
        print("\nParsing concluído com sucesso (sintaxe correta)!")

        visitor = CyamixToCVisitor()

        # Visita a árvore e gera o código C
        visitor.visit(tree)
        c_code = visitor.code


        file_base_name = sys.argv[1].split('.cyx')[0]
        write_code_to_c_file(c_code, file_base_name)

        print("\nCódigo C gerado em output.c")

if __name__ == "__main__":
    main()