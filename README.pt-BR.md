# 🧩 Compilador Cyamix

🌎 **Idiomas disponíveis:**

- [🇺🇸 English](README.md)
- [🇧🇷 Português](README.pt-BR.md)

Este projeto implementa um **compilador para a linguagem Cyamix**, utilizando o **ANTLR4** para análise léxica e sintática, e **Python** para **geração de código em C**.

---

## ⚙️ Instalando o ANTLR4

1. **Baixe o arquivo JAR do ANTLR4:**  
   👉 [https://www.antlr.org/download/antlr-4.13.2-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar)

2. Opcionalmente, mova o arquivo para uma pasta de fácil acesso:
   ```bash
   C:\antlr\antlr-4.13.2-complete.jar
   ```

---

## 📦 Instalando dependências Python

Antes de executar o compilador, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

---

## 🧠 Regenerar arquivos do ANTLR (Lexer, Parser, Visitor, Listener)

Sempre que modificar o arquivo **`Cyamix.g4`**, é necessário regenerar os artefatos do ANTLR:

```bash
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener Cyamix.g4
```

📁 Isso irá gerar (ou atualizar) os seguintes arquivos:

- `CyamixLexer.py`
- `CyamixParser.py`
- `CyamixListener.py`
- `CyamixVisitor.py`

---

## 🧩 Extensão recomendada para VS Code

Para facilitar o desenvolvimento da gramática:

> **ANTLR4 grammar syntax support**
> Autor: _Mike Lischke_

🟢 Esta extensão adiciona **realce de sintaxe**, **navegação entre regras** e **validação de gramática** diretamente no VS Code.

---

## 🐞 Depuração do compilador

Para depurar o processo de compilação:

1. Abra o projeto no **VS Code**
2. Edite o arquivo `debugging.py` e defina o nome do arquivo `.cyx` que deseja testar
3. Execute o projeto no **modo Debug (F5)**

Isso permite inspecionar cada etapa da análise e geração de código C.

---

## 🧱 Estrutura do projeto

```plaintext
CYAMIX-LANGUAGE-ANTLR4/
├─ compiler/
│  ├─ code_generator.py      # Gera o código C equivalente a partir da AST do Cyamix
│  ├─ compiler.py            # Lógica principal e orquestração do compilador
│  ├─ error_listener.py      # Listener de erros personalizado do ANTLR
│  └─ semantic_analyzer.py   # Validação semântica e verificação de símbolos
│
├─ generated/                # Arquivos C gerados automaticamente para testes
│  └─ test.c ...
│
├─ grammar/                  # Gramática e arquivos Python gerados pelo ANTLR
│  ├─ Cyamix.g4              # Definição da gramática da linguagem Cyamix
│  ├─ CyamixLexer.py
│  ├─ CyamixParser.py
│  ├─ CyamixListener.py
│  └─ CyamixVisitor.py
│
├─ tests/                    # Scripts e programas de teste para validação
│  └─ test.cyx ...
├─ .gitignore                # Regras de exclusão do Git
├─ debugging.py              # Script auxiliar de depuração
├─ main.py                   # Arquivo principal que executa o compilador
└─ requirements.txt          # Bibliotecas necessárias para rodar o compilador
```

---

## 🏗️ Fluxo do compilador

1. **Análise léxica:** divide o código-fonte em tokens (`CyamixLexer`)
2. **Análise sintática:** constrói a árvore sintática (`CyamixParser`)
3. **Verificação de erros:** usa `CyamixErrorListener` para capturar erros
4. **Geração de código:** `CyamixToCVisitor` percorre a árvore e gera código em C
5. **Saída:** o código C é salvo em arquivos `.c`, compiláveis com `gcc` ou `clang`

---

## 🚀 Exemplo de uso

```bash
python main.py tests/test.cyx
```

Se a sintaxe estiver correta, o compilador exibirá:

```text
Iniciando análise de test.cyx...
Análise concluída com sucesso (sintaxe válida)!
Código C gerado em test.c
```

---

## 🧰 Compilar o código C gerado

Após gerar o arquivo `.c`, compile-o usando GCC ou um compilador online:

[Compilador C Online](https://www.onlinegdb.com/online_c_compiler)

```bash
gcc test.c -o test.exe
./test.exe
```

---

## 📄 Principais arquivos

| Arquivo                        | Descrição                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| **main.py**                    | Ponto de entrada do compilador. Lê o arquivo `.cyx`, executa o parser e gera o código C. |
| **Cyamix.g4**                  | Define a gramática da linguagem Cyamix (regras léxicas e sintáticas).                    |
| **compiler/analyzer.py**       | Executa o parser e retorna a árvore sintática.                                           |
| **compiler/code_generator.py** | Implementa o Visitor que converte código Cyamix em código C.                             |
| **debugging.py**               | Script auxiliar para testar o compilador no modo debug.                                  |
| **generated/**                 | Pasta contendo os arquivos C gerados automaticamente.                                    |
| **grammar/**                   | Pasta contendo o parser e lexer gerados pelo ANTLR.                                      |

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de pesquisa.
Distribuído sob a **licença MIT**.
