# 1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_letras(texto):
    frecuencias = {}
    for letra in texto.replace(" ", ""):
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


# Estoy usando "texto.replace(' ', '')" para eliminar todos los espacios del texto
# antes de recorrerlo, así el bucle no los considera.
# Luego, con "frecuencias.get(letra, 0)" obtengo el valor actual de esa letra
# en el diccionario (o 0 si todavía no existe) y le sumo 1.

# Ejemplo para comprobar que funciona

texto = "Me llamo Maria"

resultado = contar_letras(texto)

print(resultado)

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def doble(numero):
    return numero*2
lista_doble = list(map(doble, lista_numeros))

print(lista_doble)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# Recorro cada palabra de la lista con for y compruebo si la palabra objetivo
# está (en este caso ia) contenida dentro de ella usando el operador "in". Si está,
# la añado a la lista de resultados con "append".

lista_palabras = ["Maria", "Es", "Genial"]

def buscar_palabras(lista, objetivo):
    resultado = []

    for palabra in lista:
        if objetivo in palabra:
            resultado.append(palabra)

    return resultado

print(buscar_palabras(lista_palabras, "ia"))

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

lista_numeros1 = [7, 8, 9, 10, 11, 12]
lista_numeros2 = [1, 2, 3, 4, 5, 6]

def diferencia (num1, num2):
    return num1 - num2

diferencia_map = list(map( diferencia,lista_numeros1, lista_numeros2))

print (diferencia_map)

#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

notas = [4, 5, 6, 8, 10]

def calcular_aprobado(lista, nota_aprobado=5):
    media = sum(lista) / len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return media, estado

resultado = calcular_aprobado(notas)
print(resultado)

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1: #Caso base. Si n no es ni 0 ni 1 entonces se hace else llamandose a si misma.
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

# Primero he definido una lista de tuplas.
# Después uso map() para recorrer cada tupla de la lista.
# Con lambda accedo a los elementos de cada tupla mediante sus posiciones y los convierto en un string usando un formato de texto.
# Por último, uso list() para convertir el resultado de map() en una lista normal.

lista_tuplas = [
    ("Maria", 25),
    ("Juan", 30),
    ("Ana", 22)
]

def convertir_tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: f"{tupla[0]} - {tupla[1]}", lista_tuplas))

resultado = convertir_tuplas_a_strings(lista_tuplas)

print(resultado)

#8.Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

# Primero he puesto que los números introducidos tienen que ser float. Partiendo de esta base he contemplado dos errores. El primero (ValueError) por si escribe el número (Ocho, 5a..). El segundo (ZeroDivisionError) error se da si se intenta dividir entre 0. 

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        resultado = num1 / num2

    except ValueError:
        print("Error: debes introducir un valor numérico.")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")

    else:
        print(f"División exitosa. El resultado es: {resultado}")

dividir_numeros()

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

lista_mascotas =  ["Perro", "Conejo", "Mapache", "Tigre", "Gato","Serpiente Pitón","Pez", "Cocodrilo", "Oso"]

prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def permitida(mascota):
    return mascota not in prohibidas

def excluyentes(lista):
    return list(filter(permitida, lista))

print(excluyentes(lista_mascotas))

#10.Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

lista_numeros3 = [1, 2, 3, 4, 5]
lista_vacia = [] #Ejemplo para comprobar que el error funciona

class ListaVaciaError(Exception):# Creo una clase donde está incluida la excepción personalizada
    pass

def calcular_promedio(lista):
    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía.")# raise lanza la excepción

    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio(lista_vacia)
    print("El promedio es:", promedio)

except ListaVaciaError as e: #guarda la excepción en "e" para lanzar el mensaje de Error 
    print("Error:", e)



#11.
#12.
#13.
#14.
#15.
#16.
#17.
#18.
#19.
#20.
#21.
#22.
#23.
#24.
#25.
#26.
#27.
#28.
#29.
#30.
#31.
#32.
#33.
#34.
#35.
#36.
#37.
#38.
#39.
#40.