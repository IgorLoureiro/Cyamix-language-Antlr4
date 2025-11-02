import sys
import glob
import os
from antlr4 import FileStream, CommonTokenStream
from CyamixLexer import CyamixLexer
from CyamixParser import CyamixParser
from compiler.utils import write_code_to_c_file
from compiler.code_generator import CyamixToCVisitor
from error_listener import CyamixErrorListener
from semantic_analyzer import SemanticAnalyzer

files_to_process = []

def run_parser(file_path: str):
    """
    Runs the parser (SYNTAX) and returns the TREE and SYNTAX ERRORS.
    """
    try:
        input_stream = FileStream(file_path, encoding='utf-8')
    except FileNotFoundError:
        return None, [f"Error: File not found at path: {file_path}"]
    except Exception as e:
        return None, [f"Error opening file: {e}"]

    lexer = CyamixLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CyamixParser(stream)

    error_listener = CyamixErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    return tree, error_listener.errors

def process_file(file_path: str):
    """Orchestrates the analysis for a single file and prints the result."""
    print(f"\n--- Starting compilation of {os.path.basename(file_path)} ---")
    
    print("Running Lexical and Syntactic Analysis...")
    tree, syntax_errors = run_parser(file_path)

    if syntax_errors:
        print("Analysis failed! Syntax errors found:")
        for error in syntax_errors:
            print(f"    {error}")
        return
    
    print("Lexical and Syntactic Analysis passed successfully.")
        
    print("Running Semantic Analysis...")
    
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)
    semantic_errors = analyzer.semantic_errors
    
    if semantic_errors:
        print("Analysis failed! Semantic errors found:")
        for error in semantic_errors:
            print(f"    {error}")
    else:
        print("Semantic Analysis passed successfully!")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_or_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        print(f"Processing all files in directory: {input_path}")
        files_to_process = sorted(glob.glob(os.path.join(input_path, '*.cyx')))
        
        if not files_to_process:
             print("No .cyx files found in the specified directory.")
             sys.exit(0)
             
        for file_path in files_to_process:
            process_file(file_path)
            
    elif os.path.isfile(input_path):
        process_file(input_path)
        
    else:
        print(f"Error: Path not found: {input_path}")
        sys.exit(1)

        visitor = CyamixToCVisitor()

        visitor.visit(tree)
        c_code = visitor.code


        file_base_name = sys.argv[1].split('.cyx')[0]
        write_code_to_c_file(c_code, file_base_name)

        print("\nGenerated code in /generated/" + file_base_name + ".c")

if __name__ == "__main__":
    main()