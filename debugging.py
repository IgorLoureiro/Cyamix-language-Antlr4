import os
import glob
from compiler.compiler import compile_file

# Caminho do arquivo ou diretório de teste
TEST_FILE = "tests/test.cyx"
# TEST_DIR = "tests"  # se quiser processar todos os .cyx do diretório

def main():
    input_path = TEST_FILE  # ou TEST_DIR

    if os.path.isfile(input_path):
        print(f"\n--- Compiling {os.path.basename(input_path)} ---")
        success, messages = compile_file(input_path)
        for msg in messages:
            print(msg)

    elif os.path.isdir(input_path):
        files = sorted(glob.glob(os.path.join(input_path, "*.cyx")))
        if not files:
            print("No .cyx files found in directory.")
            return
        for f in files:
            print(f"\n--- Compiling {os.path.basename(f)} ---")
            success, messages = compile_file(f)
            for msg in messages:
                print(msg)

    else:
        print(f"Error: Path not found: {input_path}")

if __name__ == "__main__":
    main()
