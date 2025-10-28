import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser

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

if __name__ == "__main__":
    main()