# StatsLang

StatsLang es un proyecto académico desarrollado para el curso de **Teoría de Compiladores**. Consiste en el diseño e implementación parcial de un lenguaje de dominio específico orientado a consultas estadísticas simples, utilizando **ANTLR4**, **Python** y una generación básica de representación intermedia.

El proyecto permite analizar archivos con extensión `.stats`, reconocer instrucciones del lenguaje, generar tokens, construir el árbol de parseo, recorrerlo mediante un visitor y producir una salida intermedia básica.

## Objetivo del proyecto

El objetivo principal de StatsLang es aplicar conceptos fundamentales de compiladores mediante la construcción de un lenguaje pequeño, incluyendo:

* Definición formal de una gramática.
* Análisis léxico.
* Análisis sintáctico.
* Manejo de errores.
* Construcción del árbol de parseo.
* Recorrido del árbol mediante visitor.
* Generación básica de representación intermedia.
* Organización de ejemplos válidos e inválidos.

## Tecnologías utilizadas

* Python
* ANTLR4
* Java Runtime Environment
* ANTLR4 Python Runtime
* llvmlite
* Graphviz
* Gramáticas `.g4`

## Características principales

StatsLang soporta instrucciones para:

* Cargar archivos de datos.
* Realizar consultas estadísticas.
* Usar funciones de agregación.
* Definir alias para resultados.
* Agregar condiciones con `where`.
* Combinar condiciones con operadores lógicos.
* Declarar histogramas simples.
* Detectar errores sintácticos básicos.

## Sintaxis del lenguaje

Para una explicación más detallada de la gramática definida en ANTLR4, revisar [`docs/grammar-overview.md`](docs/grammar-overview.md).

### Carga de archivo

```stats
load "ventas.csv";
```

### Consulta estadística

```stats
select avg(precio) where categoria = "ropa";
```

### Consulta con múltiples agregaciones

```stats
select avg(nota) as promedio, max(nota), min(nota);
```

### Histograma

```stats
histogram edad bins=5;
```

## Funciones soportadas

StatsLang reconoce las siguientes funciones de agregación:

* `avg`
* `sum`
* `count`
* `min`
* `max`

## Operadores soportados

### Operadores de comparación

* `=`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

### Operadores lógicos

* `and`
* `or`

## Estructura del proyecto

```txt
StatsLang/
  docs/
    grammar-overview.md

  examples/
    invalid/
      error1.stats
    valid/
      ejemplo1.stats
      ejemplo2.stats

  generated/
    Stats.interp
    Stats.tokens
    StatsLexer.interp
    StatsLexer.py
    StatsLexer.tokens
    StatsListener.py
    StatsParser.py
    StatsVisitor.py

  grammar/
    Stats.g4

  outputs/
    ejemplo1_output.txt
    ejemplo2_output.txt
    error1_output.txt

  src/
    backend/
      codegen.py
      stats_visitor.py
    frontend/
      error_listener.py
      parser_driver.py
    main.py

  .gitignore
  README.md
  requirements.txt
```

## Descripción de carpetas

### `grammar/`

Contiene la gramática principal del lenguaje:

```txt
Stats.g4
```

Este archivo define las reglas del parser, los tokens del lexer, las palabras reservadas, operadores, identificadores, números, cadenas y comentarios.

### `generated/`

Contiene los archivos generados automáticamente por ANTLR4 a partir de `grammar/Stats.g4`.

Se incluyen en el repositorio para facilitar la ejecución y revisión del proyecto académico sin necesidad de regenerarlos manualmente.

### `src/frontend/`

Contiene la lógica encargada de ejecutar el análisis léxico y sintáctico.

Archivos principales:

* `parser_driver.py`: ejecuta el lexer, parser y muestra el árbol de parseo.
* `error_listener.py`: maneja errores personalizados de sintaxis.

### `src/backend/`

Contiene la lógica posterior al parseo.

Archivos principales:

* `stats_visitor.py`: recorre el árbol de parseo generado por ANTLR.
* `codegen.py`: genera una representación intermedia básica usando llvmlite.

### `examples/`

Contiene archivos `.stats` de prueba.

* `examples/valid/`: ejemplos sintácticamente válidos.
* `examples/invalid/`: ejemplos con errores esperados.

### `outputs/`

Contiene evidencias de ejecución del proyecto.

Incluye las salidas generadas para los ejemplos válidos e inválidos.

### `docs/`

Contiene documentación técnica adicional del proyecto.

- [`grammar-overview.md`](docs/grammar-overview.md): explica la estructura de la gramática, las reglas principales del parser, los tokens del lexer, ejemplos válidos e inválidos, y el flujo general de análisis.

## Ejemplos incluidos

### `ejemplo1.stats`

```stats
load "ventas.csv";
select avg(precio) where categoria = "ropa";
```

Este ejemplo carga un archivo y ejecuta una consulta estadística con una función de agregación y una condición.

### `ejemplo2.stats`

```stats
load "alumnos.csv";
select avg(nota) as promedio, max(nota), min(nota);
histogram edad bins=5;
```

Este ejemplo carga un archivo, ejecuta una consulta con varias funciones de agregación y declara un histograma.

### `error1.stats`

```stats
load alumnos.csv;
```

Este ejemplo genera error porque el nombre del archivo debe estar entre comillas.

Forma correcta:

```stats
load "alumnos.csv";
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Axel-Pariona/StatsLang.git
cd StatsLang
```

Crear un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar todos los ejemplos:

```bash
python -m src.main
```

Ejecutar un archivo específico:

```bash
python -m src.main examples/valid/ejemplo1.stats
```

```bash
python -m src.main examples/valid/ejemplo2.stats
```

```bash
python -m src.main examples/invalid/error1.stats
```

## Salida esperada

Durante la ejecución, el programa muestra:

* Archivo analizado.
* Árbol de parseo.
* Recorrido del árbol.
* Instrucciones reconocidas.
* Representación intermedia básica.
* Errores sintácticos o semánticos, si existen.

Ejemplo parcial de salida:

```txt
══════════════════════════════════════════════════
Analizando archivo: examples/valid/ejemplo1.stats
══════════════════════════════════════════════════

Árbol de parseo:
(prog (stmt (loadStmt load "ventas.csv") ;) ...)

Recorriendo árbol de parseo
LOAD → ventas.csv
IR: print('Load dataset "ventas.csv"')
SELECT → selectavg(precio)wherecategoria="ropa"
IR: print('SELECT query')
```

## Evidencias de ejecución

Las evidencias generadas se encuentran en la carpeta `outputs/`.

```txt
outputs/
  ejemplo1_output.txt
  ejemplo2_output.txt
  error1_output.txt
```

Estas salidas permiten revisar el comportamiento del analizador con ejemplos válidos e inválidos.

## Generación de archivos ANTLR

Los archivos generados ya se incluyen en la carpeta `generated/`.

Si se desea regenerarlos manualmente, se puede ejecutar el siguiente comando desde la raíz del proyecto:

```bash
antlr4 -Dlanguage=Python3 -visitor -o generated -Xexact-output-dir grammar/Stats.g4
```

También puede usarse directamente el archivo `.jar` de ANTLR:

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o generated -Xexact-output-dir grammar/Stats.g4
```

## Flujo general del compilador

```txt
Archivo .stats
  ↓
Lexer generado por ANTLR4
  ↓
Tokens
  ↓
Parser generado por ANTLR4
  ↓
Árbol de parseo
  ↓
Visitor
  ↓
Representación intermedia básica
```

## Alcance del proyecto

El proyecto implementa una versión académica inicial de un lenguaje estadístico.

Actualmente incluye:

* Gramática funcional en ANTLR4.
* Lexer generado.
* Parser generado.
* Visitor generado.
* Análisis de ejemplos válidos.
* Manejo de ejemplo inválido.
* Recorrido del árbol de parseo.
* Generación básica de representación intermedia.
* Evidencias de ejecución.

## Limitaciones

* No ejecuta consultas reales sobre archivos CSV.
* No valida la existencia real de columnas.
* No implementa una tabla de símbolos completa.
* No realiza inferencia de tipos.
* No calcula resultados estadísticos reales.
* La representación intermedia generada es básica.
* El proyecto está orientado principalmente al análisis léxico, sintáctico y recorrido del árbol.

## Posibles mejoras

* Implementar análisis semántico completo.
* Validar existencia de datasets y columnas.
* Leer archivos CSV reales.
* Ejecutar funciones estadísticas sobre datos.
* Implementar tabla de símbolos.
* Mejorar los mensajes de error.
* Agregar pruebas automatizadas.
* Soportar expresiones aritméticas.
* Agregar instrucciones como `group by` y `order by`.
* Generar una representación intermedia más completa.

## Estado del proyecto

Proyecto académico funcional en etapa inicial.

El analizador reconoce correctamente ejemplos válidos, detecta errores en entradas inválidas y muestra el proceso de análisis mediante árbol de parseo, visitor y representación intermedia básica.

## Autores

* Omar Junior Acuña Villegas
* Axel Yamir Pariona Rojas
* José Javier Villanueva Aramburú
