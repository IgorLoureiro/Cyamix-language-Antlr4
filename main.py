import sys
from antlr4 import FileStream, CommonTokenStream
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser

from error_listener import CyamixErrorListener

def run_parser(file_path: str) -> list[str]:
    """
    This is the dedicated parsing function.
    It contains the core parsing logic.
    It takes a file path, runs the parser, and returns a list of errors.
    """
    
    try:
        input_stream = FileStream(file_path, encoding='utf-8')
    except FileNotFoundError:
        return [f"Error: File not found at path: {file_path}"]
    except Exception as e:
        return [f"Error opening file: {e}"]

    lexer = CyamixLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CyamixParser(stream)

    error_listener = CyamixErrorListener()
    parser.removeErrorListeners() 
    parser.addErrorListener(error_listener)

    tree = parser.program()

    return error_listener.errors

def main():
    """
    Main entry point for the script.
    Handles command-line arguments and prints the final result.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <source.cyx>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Starting parsing of {file_path}...")

    errors = run_parser(file_path)

    if errors:
        print("\nParsing failed! Errors found:")
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("\nParsing completed successfully (correct syntax)!")

if __name__ == "__main__":
    main()