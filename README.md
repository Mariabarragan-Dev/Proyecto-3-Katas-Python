# Proyecto 3: Katas Python

Este repositorio recoge la resolución de los 40 ejercicios (katas) de Python que nos pidieron para practicar y afianzar lo aprendido durante el módulo.

**Autora:** María Barragán Estévez

---

## De qué va este proyecto

Son 40 ejercicios sueltos de Python, cada uno centrado en algo distinto. A lo largo de todos ellos he ido tocando:

- Tipos de datos básicos y funciones que ya trae Python de serie
- Listas, diccionarios, tuplas y sets, y sus métodos
- Condicionales (`if`, `elif`, `else`)
- Bucles (`for`) y comprensión de listas
- Funciones, funciones lambda y las famosas `map()`, `filter()` y `reduce()`
- Manejo de errores con `try`/`except`/`else`, incluidas excepciones creadas por mí
- Clases y programación orientada a objetos
- Algún módulo de Python como `math` y `functools`
- Intentar dejar el código limpio, con nombres de variables que se entiendan y comentarios donde hacía falta

---

## Estructura del repositorio:

```
Proyecto-3-Katas-Python/
│
├── katas.py       # Archivo con los 40 ejercicios resueltos
└── README.md      # Este archivo
```

## Cómo ejecutar el proyecto:

## 1. Clona el repositorio:
```
git clone <https://github.com/Mariabarragan-Dev/Proyecto-3-Katas-Python.git>
```
## 2. Entra en la carpeta del proyecto:
```
cd Proyecto-3-Katas-Python
```
## 3. Ejecuta el archivo con Python (versión 3.x):
```
python katas.py
```
Los ejercicios (8, 11, 25, 31, 32, 37, 38, 40) piden datos por teclado (input()), por lo que el programa se detendrá esperando que introduzcas un valor en la consola.

## Índice de ejercicios
| # | Enunciado (resumen) | Conceptos clave |
|---|----------------------|------------------|
| 1 | Frecuencia de letras en una cadena | Diccionarios, `.replace()` |
| 2 | Doble de cada valor de una lista | `map()` |
| 3 | Palabras que contienen una palabra objetivo | Bucle `for`, `in` |
| 4 | Diferencia entre valores de dos listas | `map()` con dos listas |
| 5 | Media y estado aprobado/suspenso | Parámetro opcional, tuplas |
| 6 | Factorial recursivo | Recursividad |
| 7 | Lista de tuplas a lista de strings | `map()`, `lambda` |
| 8 | División de dos números con manejo de errores | `try`/`except`/`else` |
| 9 | Excluir mascotas prohibidas | `filter()` |
| 10 | Promedio de una lista con excepción personalizada | Excepciones personalizadas (`class ... (Exception)`) |
| 11 | Validar edad introducida por el usuario | `try`/`except`, validación de rango |
| 12 | Longitud de cada palabra de una frase | `map()`, `.split()` |
| 13 | Tuplas mayúscula/minúscula de un set | `map()`, sets |
| 14 | Palabras que empiezan por una letra | `filter()`, función anidada (closure) |
| 15 | Sumar 3 a cada número de una lista | `lambda`, `map()` |
| 16 | Palabras más largas que n | `filter()`, `lambda` |
| 17 | Lista de dígitos a número completo | `reduce()` |
| 18 | Estudiantes con nota ≥ 90 | `filter()`, lista de diccionarios |
| 19 | Filtrar números impares | `lambda`, `filter()` |
| 20 | Filtrar solo valores `int` de una lista mixta | `filter()`, `isinstance()` |
| 21 | Cubo de un número | `lambda` |
| 22 | Producto total de una lista | `reduce()` |
| 23 | Concatenar lista de palabras | `reduce()` |
| 24 | Diferencia total de una lista | `reduce()` |
| 25 | Contar caracteres de una cadena | `len()`, `input()` |
| 26 | Resto de la división entre dos números | `lambda` |
| 27 | Promedio de una lista | `sum()`, `len()` |
| 28 | Primer elemento duplicado de una lista | Bucle `for`, listas auxiliares |
| 29 | Enmascarar caracteres excepto los últimos 4 | Slicing, `str()` |
| 30 | Comprobar si dos palabras son anagramas | `sorted()`, `.replace()` |
| 31 | Buscar nombre en lista con excepción | `Exception`, `try`/`except` |
| 32 | Buscar puesto de un empleado por nombre completo | Lista de diccionarios, bucle `for` |
| 33 | Sumar elementos de dos listas | `lambda`, `zip()` |
| 34 | Clase `Arbol` (POO) | Clases, métodos, atributos |
| 35 | Clase `UsuarioBanco` (POO) | Clases, excepciones personalizadas |
| 36 | Función `procesar_texto` (contar/reemplazar/eliminar) | `*args`, funciones auxiliares |
| 37 | Indicar momento del día según la hora | Condicionales encadenados |
| 38 | Calificación en texto según nota numérica | Condicionales, rangos |
| 39 | Área de figuras geométricas | Tuplas, módulo `math` |
| 40 | Calcular precio final con cupón de descuento | Condicionales, `try`/`except` |

---

## Enfoque y pasos seguidos durante el proyecto:

- He intentado seguir cada enunciado al pie de la letra. Cuando pedía usar una función en concreto (`map()`, `filter()`, `reduce()`, `lambda`), la he usado en vez de tirar directamente de un bucle `for`, aunque a veces hubiera sido más rápido.
- En los ejercicios donde no podía usar `lambda`, he creado funciones normales con `def`. En algún caso (como el 14) usé una función dentro de otra función para no tener que usar variables globales, que sé que no es buena práctica.
- En los ejercicios con manejo de errores (8, 10, 11, 31, 35, 37, 38, 40) he probado el código tanto metiendo datos correctos como datos que sabía que iban a fallar, para asegurarme de que los mensajes de error salían bien y el programa no se rompía.
- En el ejercicio 35 (la clase `UsuarioBanco`) me di cuenta de que, si sigo los números que da el propio enunciado, Bob se queda con 70 (50 + 20) y luego se le pide transferir 80, así que no le llega el saldo. Al principio pensé que tenía un error en mi código, pero en realidad es que la validación de saldo insuficiente está funcionando como debería. Decidí dejar el caso de uso tal cual lo pide el enunciado y controlar ese error con `try`/`except`, en vez de cambiar los números para que "cuadrara".
- He usado IA puntualmente para resolver dudas de sintaxis y para encontrar errores tontos (fallos de indentación, nombres de función mal escritos, cómo funciona `*args`...), pero todo el código lo he entendido y revisado línea a línea antes de darlo por bueno.

---

## Cómo he comprobado que funciona

Debajo de cada función he dejado uno o varios `print()` con datos de ejemplo, así que al ejecutar `katas.py` de tirón se ve por consola el resultado de los 40 ejercicios sin tener que hacer nada más (salvo los que piden `input()`, claro).

---

## Con qué está hecho

- **Python 3.13**
- Dos módulos de Python: `math` y `functools`

---

