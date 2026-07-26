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



#8.
#9.
#10.
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