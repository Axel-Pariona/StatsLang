grammar Stats;

// ----------------- PARSER RULES -----------------
prog: stmt* EOF ;

stmt    // Programa principal
    : loadStmt SEMI
    | queryStmt SEMI
    | histogramStmt SEMI
    ;

loadStmt
    : LOAD STRING
    ;

queryStmt
    : SELECT aggList (WHERE boolExpr)?
    ;

aggList
    : aggExpr (COMMA aggExpr)*
    ;

aggExpr
    : aggFunc LPAREN (IDENT | STAR) RPAREN (AS IDENT)?
    ;

aggFunc   // Funciones de agregación
    : AVG | SUM | COUNT | MIN | MAX
    ;

histogramStmt    // Sentencia de histograma
    : HISTOGRAM IDENT (BINS EQ NUMBER)?
    ;

// Expresiones booleanas (supports and/or with precedence)
boolExpr
    : boolExpr AND boolExpr
    | boolExpr OR boolExpr
    | LPAREN boolExpr RPAREN
    | comparison
    ;

comparison
    : IDENT comparator value
    ;

comparator   // Define los operadores de comparación
    : EQ | NEQ | GT | LT | GTE | LTE
    ;

value
    : NUMBER
    | STRING
    ;

// ----------------- LEXER RULES -----------------
// Keywords (case-insensitive)
// Cada palabra clave se puede escribir en mayúsculas o minúsculas
LOAD : [lL][oO][aA][dD] ;
SELECT : [sS][eE][lL][eE][cC][tT] ;
WHERE : [wW][hH][eE][rR][eE] ;
AS : [aA][sS] ;
AVG : [aA][vV][gG] ;
SUM : [sS][uU][mM] ;
COUNT : [cC][oO][uU][nN][tT] ;
MIN : [mM][iI][nN] ;
MAX : [mM][aA][xX] ;
HISTOGRAM : [hH][iI][sS][tT][oO][gG][rR][aA][mM] ;
BINS : [bB][iI][nN][sS] ;
AND : [aA][nN][dD] ;
OR : [oO][rR] ;

// Symbols   (define los simbolos que se usara en el lenguaje)
SEMI : ';' ;
COMMA : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
EQ : '=' ;
NEQ : '!=' ;
GT : '>' ;
LT : '<' ;
GTE : '>=' ;
LTE : '<=' ;
STAR : '*' ;

STRING   // Cadena de caracteres
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    ;

NUMBER   // Número real
    : [0-9]+ ('.' [0-9]+)?
    ;

// Identificadores (nombres de las columnas)
IDENT
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

// Comentarios y espacios de lineas en blanco
LINE_COMMENT
    : '--' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
