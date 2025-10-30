# 🧩 Cyamix Compiler

🌎 Available languages:

- [🇺🇸 English](README.md)
- [🇧🇷 Português](README.pt-BR.md)

This project implements a **compiler for the Cyamix language**, using **ANTLR4** for lexical and syntactic analysis, and **Python** for C code generation.

---

## ⚙️ Installing ANTLR4

1. **Download the ANTLR4 JAR file**:  
   [https://www.antlr.org/download/antlr-4.13.2-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar)

2. Optionally, move the file to an easily accessible folder, such as:
   ```
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

Whenever you modify the **`Cyamix.g4`** file, you need to regenerate the ANTLR artifacts:

```bash
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener Cyamix.g4
```

📁 This will generate (or update) the following files:

- `CyamixLexer.py`
- `CyamixParser.py`
- `CyamixListener.py`
- `CyamixVisitor.py`
- `Cyamix.tokens`
- `Cyamix.interp`

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

```
cyamix_compiler/
├─ Cyamix.g4                # ANTLR4 grammar for the Cyamix language
├─ generated/               # Automatically generated files (Lexer, Parser, Visitor, Listener)
├─ compiler/
│  ├─ analyzer.py           # Performs syntactic and semantic analysis
│  ├─ code_generator.py     # Visitor that traverses the AST and generates C code
│  └─ utils.py              # Helper functions (e.g., save files)
├─ main.py                  # Compiler entry point
├─ debugging.py             # Auxiliary script for debugging
└─ requirements.txt         # Project dependencies
```

---

## 🏗️ Compiler flow

1. **Lexical analysis:** splits the source code into tokens (`CyamixLexer`)
2. **Syntactic analysis:** builds the parse tree (`CyamixParser`)
3. **Error checking:** uses `MyErrorListener` to capture syntax errors
4. **Code generation:** `CyamixToCVisitor` traverses the tree and produces C code
5. **Output:** the generated C code is saved to `output.c`, which can be compiled with `gcc` or `clang`

---

## 🚀 Example usage

```bash
python main.py example.cyx
```

If the syntax is correct, the compiler will display:

```
Starting parsing of example.cyx...
Parsing completed successfully (valid syntax)!
C code generated in output.c
```

---

## 🧰 Compile the generated C code

After generating the `output.c` file, compile it using GCC:

```bash
gcc output.c -o program.exe
```

And run:

```bash
./program.exe
```

---

## 📄 Main files explained

| File                           | Purpose                                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------------------- |
| **main.py**                    | Compiler entry point. Reads the `.cyx` file, runs the lexer/parser, and invokes the code generator. |
| **Cyamix.g4**                  | Defines the Cyamix language grammar (lexical and syntactic rules).                                  |
| **compiler/analyzer.py**       | Executes the parser and returns the parse tree.                                                     |
| **compiler/code_generator.py** | Implements the Visitor that traverses the tree and converts Cyamix code to C.                       |
| **compiler/utils.py**          | Contains helper functions (e.g., saving the generated C code).                                      |
| **debugging.py**               | Auxiliary script to test the compiler in VS Code debug mode.                                        |
| **generated/**                 | Folder containing the automatically generated ANTLR files (do not edit manually).                   |

---

## 📄 License

This project was developed for educational and research purposes.  
Distributed under the **MIT License**.
