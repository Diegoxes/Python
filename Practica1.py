"Parte 1"

nombre = input("Ingresa un nombre: ")
edad = int(input("Ingresa tu edad: "))

print("El nombre es de tipo " + str(type(nombre)))
print("La edad es de tipo " + str(type(edad)))


"Pedir nombre de trabajadores y agregarlos a una lista"

trabajadores = []

for _ in range(2):
    nombre = input("Ingrese el nombre del trabajador: ")
    edad = int(input("Ingrese la edad del trabajador: "))
    trabajadores.append((nombre, edad))

print(trabajadores)


"Mostrar la suma de las edades"

suma_edades = trabajadores[0][1] + trabajadores[1][1]
print("Suma de las edades de los trabajadores:", suma_edades)

"Parte 2"

import random

"Crear una lista con 10 valores random"
numeros = []
for _ in range(10):
    numeros.append(random.randint(1, 100))

"Llenar otra lista con los cubos de los valores"
cubos = [num ** 3 for num in numeros]

# Llenar una lista nueva con los cuadrados de los valores
cuadrados = [num ** 2 for num in numeros]

# Mostrar de manera inversa la suma de ambas listas
suma_inversa = sum([cubos[i] for i in range(len(cubos)-1, -1, -1)]) + sum(cuadrados[j] for j in range(len(cuadrados)-1,-1,-1))


print("Suma inversa de las listas:", suma_inversa)



"Parte 3"

# Crear un diccionario con los keys de nombre, apellidos, edad y dni
persona = {
    "nombre": "",
    "apellidos": "",
    "edad": "",
    "dni": ""
}

# Pedir los valores por consola
persona["nombre"] = input("Ingrese su nombre: ")
persona["apellidos"] = input("Ingrese sus apellidos: ")
persona["edad"] = input("Ingrese su edad: ")
persona["dni"] = input("Ingrese su DNI: ")

"Mostrar solo los values del diccionario"
print("Values del diccionario:", list(persona.values()))

"Agregar un key adicional profesion y su valor"
persona["profesion"] = input("Ingrese su profesión: ")

"Eliminar el key dni y mostrar el nuevo diccionario"
del persona["dni"]
print("Nuevo diccionario:", persona)