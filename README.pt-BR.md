# 🧩 Compilador Cyamix

🌎 Idiomas disponíveis:

- [🇺🇸 English](README.md)
- [🇧🇷 Português](README.pt-BR.md)

Este projeto implementa um **compilador para a linguagem Cyamix**, utilizando **ANTLR4** para análise léxica e sintática, e **Python** para geração de código C.

---

## ⚙️ Instalação do ANTLR4

1. **Baixe o JAR do ANTLR4**:
   [https://www.antlr.org/download/antlr-4.13.2-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar)

2. Opcionalmente, mova o arquivo para uma pasta de fácil acesso, como:
   ```
   C:\antlr\antlr-4.13.2-complete.jar
   ```

---

## 📦 Instalar dependências Python

Antes de rodar o compilador, instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🧠 Regenerar arquivos ANTLR (Lexer, Parser, Visitor, Listener)

Sempre que você modificar o arquivo **`Cyamix.g4`**, é necessário regerar os artefatos do ANTLR:

```bash
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener Cyamix.g4
```

📁 Isso gerará (ou atualizará) os arquivos:

- `CyamixLexer.py`
- `CyamixParser.py`
- `CyamixListener.py`
- `CyamixVisitor.py`
- `Cyamix.tokens`
- `Cyamix.interp`

---

## 🧩 Extensão recomendada para VS Code

Para facilitar o desenvolvimento da gramática:

> **ANTLR4 grammar syntax support**  
> Autor: _Mike Lischke_

🟢 Essa extensão adiciona **realce de sintaxe**, **navegação entre regras** e **validação de gramática** diretamente no VSCode.

---

## 🐞 Debug do compilador

Para depurar o processo de compilação:

1. Abra o projeto no **VSCode**
2. Configure o arquivo `debugging.py` alterando o nome do arquivo `.cyx` que deseja testar
3. Execute o projeto em **modo Debug (F5)**

Isso permite inspecionar cada etapa do processo de parsing e geração de código C.

---

## 🧱 Estrutura do projeto

```
cyamix_compiler/
├─ Cyamix.g4                # Gramática ANTLR4 da linguagem Cyamix
├─ generated/               # Arquivos gerados automaticamente (Lexer, Parser, Visitor, Listener)
├─ compiler/
│  ├─ analyzer.py           # Realiza a análise sintática e semântica
│  ├─ code_generator.py     # Visitor que percorre a AST e gera código C
│  └─ utils.py              # Funções auxiliares (ex: salvar arquivos)
├─ main.py                  # Ponto de entrada do compilador
├─ debugging.py             # Script auxiliar para depuração
└─ requirements.txt         # Dependências do projeto
```

---

## 🏗️ Fluxo do compilador

1. **Análise léxica:** quebra o código-fonte em tokens (`CyamixLexer`)
2. **Análise sintática:** cria a árvore sintática (`CyamixParser`)
3. **Verificação de erros:** usa `MyErrorListener` para capturar erros de sintaxe
4. **Geração de código:** `CyamixToCVisitor` percorre a árvore e produz código C
5. **Saída:** código C é salvo em `output.c`, que pode ser compilado com `gcc` ou `clang`

---

## 🚀 Exemplo de uso

```bash
python main.py exemplo.cyx
```

Se a sintaxe estiver correta, o compilador exibirá:

```
Iniciando parsing de exemplo.cyx...
Parsing concluído com sucesso (sintaxe correta)!
Código C gerado em output.c
```

---

## 🧰 Compilar o código gerado em C

Após gerar o arquivo `output.c`, compile-o normalmente com o GCC:

```bash
gcc output.c -o programa.exe
```

E execute:

```bash
./programa.exe
```

---

## 📄 Explicação dos principais arquivos

| Arquivo                        | Função                                                                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **main.py**                    | Ponto de entrada do compilador. Faz a leitura do arquivo `.cyx`, executa o lexer, parser e chama o gerador de código. |
| **Cyamix.g4**                  | Define a gramática da linguagem Cyamix (regras léxicas e sintáticas).                                                 |
| **compiler/analyzer.py**       | Responsável por executar o parser e retornar a árvore sintática.                                                      |
| **compiler/code_generator.py** | Implementa o Visitor que percorre a árvore e converte o código Cyamix em C.                                           |
| **compiler/utils.py**          | Contém funções auxiliares (ex: salvar o código C em arquivo).                                                         |
| **debugging.py**               | Script auxiliar para testar o compilador em modo debug no VSCode.                                                     |
| **generated/**                 | Pasta onde ficam os arquivos gerados automaticamente pelo ANTLR (não edite manualmente).                              |

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e de pesquisa.  
Distribuído sob a licença **MIT**.
