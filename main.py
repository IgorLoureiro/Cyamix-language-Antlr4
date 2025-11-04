import sys
import os
import glob
from compiler.compiler import compile_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_or_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isfile(input_path):
        success, messages = compile_file(input_path)
        for msg in messages:
            print(msg)

    elif os.path.isdir(input_path):
        files = sorted(glob.glob(os.path.join(input_path, "*.cyx")))
        if not files:
            print("No .cyx files found in directory.")
            sys.exit(0)
        for f in files:
            print(f"\n--- Compiling {os.path.basename(f)} ---")
            success, messages = compile_file(f)
            for msg in messages:
                print(msg)
    else:
        print(f"Error: Path not found: {input_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
