// Cyamix.g4
grammar Cyamix;

/*
 Parser rules (no left recursion). Designed to:
 - support int, float, char, boolean
 - if ... else
 - while, do ... while, for
 - arithmetic + - * / or ÷ with correct precedence
 - logical && || !
 - comparison == != > < >= <=
 - assignments, scanf, printf
 - decimals (floats)
 - whitespace/comments skipped
 - no left recursion, no empty productions
*/

program
    : (topDecl | statement)* EOF
    ;

/* Top-level: variable declarations or function-like declarations (future) */
topDecl
    : varDecl
    ;

/* VARIABLE DECLARATION: type ID ( = expr )? ; */
varDecl
    : type ID ( '=' expr )? ';'
    ;

/* STATEMENTS */
statement
    : block
    | ifStmt
    | whileStmt
    | doWhileStmt
    | forStmt
    | assignment
    | funcCall ';'
    | ';'
    ;

/* BLOCK */
block
    : '{' (topDecl | statement)* '}'
    ;

/* IF / ELSE */
ifStmt
    : 'if' '(' expr ')' statement ( 'else' statement )?
    ;

/* WHILE */
whileStmt
    : 'while' '(' expr ')' statement
    ;

/* DO ... WHILE */
doWhileStmt
    : 'do' statement 'while' '(' expr ')' ';'
    ;

/* FOR: for ( init? ; cond? ; update? ) stmt */
forStmt
    : 'for' '(' forInit? ';' expr? ';' forUpdate? ')' statement
    ;

forInit
    : varDeclNoSemi
    | assignmentNoSemi
    ;

forUpdate
    : assignmentNoSemi (',' assignmentNoSemi)*
    ;

/* ASSIGNMENT */
assignment
    : ID '=' expr ';'
    ;

/* Assignment inside for / updates (no semicolon) */
assignmentNoSemi
    : ID '=' expr
    ;

/* VARIABLE DECLARATION inside for init (no semicolon) */
varDeclNoSemi
    : type ID ( '=' expr )?
    ;

/* FUNCTION CALL (printf/scanf or user) */
funcCall
    : ( 'printf' | 'scanf' | ID ) '(' argList? ')'
    ;

/* Arguments: expressions or references (&ID) for scanf */
argList
    : arg (',' arg)*
    ;

arg
    : expr
    | '&' ID        // reference for scanf like &x
    ;

/* EXPRESSIONS (precedence via chained rules - no left recursion) */
expr
    : logicalOrExpr
    ;

/* OR */
logicalOrExpr
    : logicalAndExpr ( '||' logicalAndExpr )*
    ;

/* AND */
logicalAndExpr
    : equalityExpr ( '&&' equalityExpr )*
    ;

/* EQUALITY == != */
equalityExpr
    : relationalExpr ( ( '==' | '!=' ) relationalExpr )*
    ;

/* RELATIONAL > < >= <= */
relationalExpr
    : additiveExpr ( ( '>' | '<' | '>=' | '<=' ) additiveExpr )*
    ;

/* ADD + - */
additiveExpr
    : multiplicativeExpr ( ( '+' | '-' ) multiplicativeExpr )*
    ;

/* MUL * / ÷ */
multiplicativeExpr
    : unaryExpr ( ( '*' | '/' | '÷' ) unaryExpr )*
    ;

/* UNARY + - ! */
unaryExpr
    : ( '!' | '+' | '-' ) unaryExpr
    | primary
    ;

/* PRIMARY: literals, identifiers, parenthesis */
primary
    : INT_LITERAL
    | FLOAT_LITERAL
    | CHAR_LITERAL
    | BOOL_LITERAL
    | STRING_LITERAL
    | ID
    | '(' expr ')'
    ;

/* TYPES */
type
    : 'int'
    | 'float'
    | 'char'
    | 'boolean'
    ;

/* --------------------
   LEXER RULES
   -------------------- */

/* Identifiers but reserve keywords via parser rules */
ID : [a-zA-Z_] [a-zA-Z_0-9]* ;

/* Literals */
INT_LITERAL
    : [0-9]+
    ;

/* float: digits . digits  (requires at least one digit on each side) */
FLOAT_LITERAL
    : [0-9]+ '.' [0-9]+
    ;

/* Char: single quoted with escape support */
CHAR_LITERAL
    : '\'' ( ~['\\\r\n] | '\\' . ) '\''
    ;

/* Boolean: true | false */
BOOL_LITERAL
    : 'true' | 'false'
    ;

/* Strings: double quoted with escapes */
STRING_LITERAL
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    ;

/* Operators / punctuation are matched as literals in parser rules for clarity.
   But we still need tokens for some single chars like & and delimiters. */
AMPERSAND : '&' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACK : '[' ;
RBRACK : ']' ;
SEMI : ';' ;
COMMA : ',' ;

/* COMMENTS and WHITESPACE */
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
WS : [ \t\r\n]+ -> skip ;