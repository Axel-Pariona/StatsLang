# Grammar Overview - StatsLang

Este documento describe la gramática principal de **StatsLang**, un lenguaje de dominio específico orientado a consultas estadísticas simples. La gramática fue definida con **ANTLR4** en el archivo `grammar/Stats.g4`.

El objetivo de esta documentación es explicar la estructura del lenguaje, las reglas principales del parser, los tokens reconocidos por el lexer y algunos ejemplos de sentencias válidas e inválidas.

## Objetivo de la gramática

La gramática de StatsLang permite reconocer instrucciones relacionadas con:

* Carga de archivos.
* Consultas estadísticas.
* Funciones de agregación.
* Condiciones booleanas.
* Declaración de histogramas.
* Manejo básico de errores sintácticos.

El lenguaje no ejecuta consultas reales sobre archivos CSV, sino que se enfoca en el análisis léxico, análisis sintáctico, recorrido del árbol de parseo y generación básica de representación intermedia.

## Regla inicial

La regla inicial del lenguaje es `prog`.

```antlr
prog: stmt* EOF;
```

Esta regla indica que un programa en StatsLang puede estar compuesto por cero o más sentencias, seguidas por el final del archivo.

## Sentencias principales

Cada instrucción del lenguaje se representa mediante la regla `stmt`.

```antlr
stmt
    : loadStmt SEMI
    | queryStmt SEMI
    | histogramStmt SEMI
    ;
```

Esto significa que StatsLang reconoce tres tipos principales de sentencias:

* `loadStmt`: carga de archivo.
* `queryStmt`: consulta estadística.
* `histogramStmt`: declaración de histograma.

Todas las sentencias deben finalizar con punto y coma `;`.

## Carga de archivos

La regla `loadStmt` permite declarar la carga de un archivo.

```antlr
loadStmt: LOAD STRING;
```

Ejemplo válido:

```stats
load "ventas.csv";
```

En esta instrucción:

* `load` es una palabra reservada.
* `"ventas.csv"` es un literal de tipo `STRING`.
* `;` indica el final de la sentencia.

Ejemplo inválido:

```stats
load ventas.csv;
```

Este caso es inválido porque el nombre del archivo no está entre comillas. El lexer reconoce `ventas` y `csv` como identificadores, pero el parser espera un `STRING`.

## Consultas estadísticas

La regla `queryStmt` permite definir consultas estadísticas mediante funciones de agregación.

```antlr
queryStmt: SELECT aggList (WHERE boolExpr)?;
```

Ejemplo válido:

```stats
select avg(precio) where categoria = "ropa";
```

Esta instrucción contiene:

* `select`: palabra reservada para iniciar una consulta.
* `avg(precio)`: función de agregación.
* `where categoria = "ropa"`: condición opcional.

## Lista de agregaciones

Una consulta puede incluir una o varias funciones de agregación.

```antlr
aggList: aggExpr (COMMA aggExpr)*;
```

Ejemplo:

```stats
select avg(nota) as promedio, max(nota), min(nota);
```

En este caso, la consulta contiene tres agregaciones:

* `avg(nota) as promedio`
* `max(nota)`
* `min(nota)`

## Expresiones de agregación

La regla `aggExpr` define una función estadística aplicada sobre una columna.

```antlr
aggExpr: aggFunc LPAREN ID RPAREN (AS ID)?;
```

Esto permite expresiones como:

```stats
avg(nota)
sum(total)
count(id)
max(precio)
min(edad)
```

También se puede usar un alias con `as`:

```stats
avg(nota) as promedio
```

## Funciones de agregación soportadas

La regla `aggFunc` reconoce las siguientes funciones:

```antlr
aggFunc
    : AVG
    | SUM
    | COUNT
    | MIN
    | MAX
    ;
```

Funciones disponibles:

* `avg`
* `sum`
* `count`
* `min`
* `max`

## Condiciones booleanas

Las consultas pueden incluir condiciones mediante `where`.

```antlr
boolExpr
    : comparison ((AND | OR) comparison)*
    ;
```

Esto permite escribir condiciones simples o combinadas.

Ejemplo con una condición:

```stats
select avg(precio) where categoria = "ropa";
```

Ejemplo con múltiples condiciones:

```stats
select sum(total) where categoria = "ropa" and precio > 100;
```

## Comparaciones

La regla `comparison` define una comparación entre una columna y un valor.

```antlr
comparison: ID comparator value;
```

Ejemplos:

```stats
categoria = "ropa"
precio > 100
edad >= 18
```

## Operadores de comparación

La regla `comparator` permite los siguientes operadores:

```antlr
comparator
    : EQ
    | NEQ
    | GT
    | LT
    | GTE
    | LTE
    ;
```

Operadores soportados:

* `=`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

## Valores

La regla `value` permite valores de tipo cadena o número.

```antlr
value
    : STRING
    | NUMBER
    ;
```

Ejemplos válidos:

```stats
"ropa"
100
25.5
```

## Histogramas

La regla `histogramStmt` permite declarar un histograma para una columna específica.

```antlr
histogramStmt: HISTOGRAM ID BINS EQ NUMBER;
```

Ejemplo válido:

```stats
histogram edad bins=5;
```

En esta instrucción:

* `histogram` indica que se desea generar un histograma.
* `edad` representa la columna.
* `bins=5` indica la cantidad de intervalos.

## Tokens principales

La gramática define tokens para palabras reservadas, operadores, identificadores, números y cadenas.

### Palabras reservadas

```antlr
LOAD: 'load';
SELECT: 'select';
WHERE: 'where';
AS: 'as';
HISTOGRAM: 'histogram';
BINS: 'bins';
```

### Funciones de agregación

```antlr
AVG: 'avg';
SUM: 'sum';
COUNT: 'count';
MIN: 'min';
MAX: 'max';
```

### Operadores lógicos

```antlr
AND: 'and';
OR: 'or';
```

### Operadores de comparación

```antlr
EQ: '=';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
```

### Literales e identificadores

```antlr
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';
```

## Comentarios y espacios en blanco

La gramática ignora espacios en blanco y comentarios.

```antlr
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
```

Esto permite escribir comentarios como:

```stats
// Cargar dataset de ventas
load "ventas.csv";
```

## Ejemplos válidos

### Ejemplo 1

```stats
load "ventas.csv";
select avg(precio) where categoria = "ropa";
```

Este ejemplo carga un archivo y ejecuta una consulta con una función de agregación y una condición.

### Ejemplo 2

```stats
load "alumnos.csv";
select avg(nota) as promedio, max(nota), min(nota);
histogram edad bins=5;
```

Este ejemplo carga un archivo, ejecuta una consulta con varias funciones de agregación y declara un histograma.

## Ejemplo inválido

```stats
load alumnos.csv;
```

Este ejemplo genera error porque el nombre del archivo debe escribirse como una cadena entre comillas:

```stats
load "alumnos.csv";
```

## Flujo de análisis

El flujo general del análisis en StatsLang es:

```txt
Archivo .stats
  ↓
Lexer generado por ANTLR
  ↓
Tokens
  ↓
Parser generado por ANTLR
  ↓
Árbol de parseo
  ↓
Visitor
  ↓
Representación intermedia básica
```

## Alcance de la gramática

La gramática actual permite validar la estructura del lenguaje y generar un árbol de parseo. Sin embargo, el proyecto no implementa todavía una ejecución real de consultas estadísticas sobre archivos CSV.

Actualmente el alcance incluye:

* Análisis léxico.
* Análisis sintáctico.
* Manejo básico de errores.
* Recorrido del árbol de parseo.
* Generación básica de IR.

## Posibles mejoras de la gramática

Algunas mejoras futuras podrían ser:

* Soporte para más tipos de datos.
* Validación semántica de columnas.
* Expresiones aritméticas.
* Agrupamiento con `group by`.
* Ordenamiento con `order by`.
* Lectura real de archivos CSV.
* Ejecución de funciones estadísticas sobre datos reales.
* Mensajes de error más descriptivos.
