import os
import glob
from antlr4 import FileStream, CommonTokenStream
from grammar.CyamixLexer import CyamixLexer
from grammar.CyamixParser import CyamixParser
from compiler.semantic_analyzer import SemanticAnalyzer
from compiler.code_generator import CyamixToCVisitor
from compiler.error_listener import CyamixErrorListener

GENERATED_DIR = "generated"


def run_parser(file_path: str):
    try:
        input_stream = FileStream(file_path, encoding='utf-8')
    except FileNotFoundError:
        return None, [f"File not found: {file_path}"]
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


def run_semantic_analysis(tree):
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)
    return analyzer.semantic_errors


def generate_c_code(tree):
    visitor = CyamixToCVisitor()
    visitor.visit(tree)
    return visitor.code


def write_c_file(code: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)


def compile_file(file_path: str):
    """
    Full compilation pipeline for a single file:
    parsing -> semantic analysis -> code generation -> write file
    Returns (success: bool, errors: list)
    """
    tree, syntax_errors = run_parser(file_path)
    if syntax_errors:
        return False, syntax_errors

    print('--- Parsig Complete ---')

    semantic_errors = run_semantic_analysis(tree)
    if semantic_errors:
        return False, semantic_errors
    
    print('--- No semantic errors, generating C file... ---')

    c_code = generate_c_code(tree)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(GENERATED_DIR, base_name + ".c")
    write_c_file(c_code, output_path)

    return True, [f"C code generated: {output_path}"]
