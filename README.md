# 🧩 Cyamix Compiler

🌎 **Available languages:**

- [🇺🇸 English](README.md)
- [🇧🇷 Português](README.pt-BR.md)

This project implements a **compiler for the Cyamix programming language**, using **ANTLR4** for lexical and syntactic analysis, and **Python** for **C code generation**.

---

## ⚙️ Installing ANTLR4

1. **Download the ANTLR4 JAR file:**  
   👉 [https://www.antlr.org/download/antlr-4.13.2-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar)

2. Optionally, move it to an easily accessible folder:
   ```bash
   C:\antlr\antlr-4.13.2-complete.jar
   ```

---

## 📦 Install Python dependencies

Before running the compiler, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Regenerate ANTLR files (Lexer, Parser, Visitor, Listener)

Whenever you modify the **`Cyamix.g4`** grammar file, you need to regenerate the ANTLR artifacts:

```bash
antlr4 -Dlanguage=Python3 -visitor -listener Cyamix.g4
```

📁 This will generate (or update) the following files:

- `CyamixLexer.py`
- `CyamixParser.py`
- `CyamixListener.py`
- `CyamixVisitor.py`

---

## 🧩 Recommended VS Code extension

To simplify grammar development:

> **ANTLR4 grammar syntax support**
> Author: _Mike Lischke_

🟢 This extension adds **syntax highlighting**, **rule navigation**, and **grammar validation** directly in VS Code.

---

## 🐞 Compiler debugging

To debug the compilation process:

1. Open the project in **VS Code**
2. Edit the `debugging.py` file and set the name of the `.cyx` file you want to test
3. Run the project in **Debug mode (F5)**

This allows you to inspect each step of the parsing and C code generation process.

---

## 🧱 Project structure

```plaintext
CYAMIX-LANGUAGE-ANTLR4/
├─ compiler/
│  ├─ code_generator.py      # Generates equivalent C code from the parsed Cyamix AST
│  ├─ compiler.py            # Main compiler logic and orchestration
│  ├─ error_listener.py      # Custom ANTLR error listener for syntax diagnostics
│  └─ semantic_analyzer.py   # Performs semantic validation and symbol checks
│
├─ generated/                # Auto-generated C output files for test programs
│  └─ test.c ...
│
├─ grammar/                  # Grammar and ANTLR-generated Python parser
│  ├─ Cyamix.g4              # ANTLR4 grammar definition for the Cyamix language
│  ├─ CyamixLexer.py
│  ├─ CyamixParser.py
│  ├─ CyamixListener.py
│  └─ CyamixVisitor.py
│
├─ tests/                    # Test scripts and sample programs (to validate translation)
│  └─ test.cyx ...
├─ .gitignore                # Git ignore rules
├─ debugging.py              # Utility script for debugging parsing and code generation
├─ main.py                   # Main file that runs the compiler
└─ requirements.txt          # Required libraries to run the compiler
```

---

## 🏗️ Compiler flow

1. **Lexical analysis:** splits the source code into tokens (`CyamixLexer`)
2. **Syntactic analysis:** builds the parse tree (`CyamixParser`)
3. **Error checking:** uses `CyamixErrorListener` to capture syntax errors
4. **Code generation:** `CyamixToCVisitor` traverses the tree and produces C code
5. **Output:** the generated C code is saved to `.c` files, which can be compiled with `gcc` or `clang`

---

## 🚀 Example usage

```bash
python main.py tests/test.cyx
```

If the syntax is correct, the compiler will display:

```text
Starting parsing of test.cyx...
Parsing completed successfully (valid syntax)!
C code generated in test.c
```

---

## 🧰 Compile the generated C code

After generating the `.c` file, compile it using GCC or an online C compiler:

[Online C Compiler](https://www.onlinegdb.com/online_c_compiler)

```bash
gcc test.c -o test.exe
./test.exe
```

---

## 📄 Main files explained

| File                           | Purpose                                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------------------- |
| **main.py**                    | Compiler entry point. Reads the `.cyx` file, runs the lexer/parser, and invokes the code generator. |
| **Cyamix.g4**                  | Defines the Cyamix language grammar (lexical and syntactic rules).                                  |
| **compiler/analyzer.py**       | Executes the parser and returns the parse tree.                                                     |
| **compiler/code_generator.py** | Implements the Visitor that traverses the tree and converts Cyamix code to C.                       |
| **debugging.py**               | Auxiliary script to test the compiler in VS Code debug mode.                                        |
| **generated/**                 | Folder containing the automatically generated C files (do not edit manually).                       |
| **grammar/**                   | Folder containing the ANTLR-generated parser and lexer.                                             |

---

## 📄 License

This project was developed for educational and research purposes.
Di
