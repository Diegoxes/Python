import math
import random

def crear_fichero():
    with open("notas.txt", "w") as file:
        tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
        numeros = [random.randint(1, 100) for _ in range(tamaño_lista)]
        file.write(",".join(map(str, numeros)))

def calcular_raices():
    with open("notas.txt", "r") as file:
        numeros = file.read().split(",")
    raices = [math.sqrt(int(num)) for num in numeros]
    with open("notas.txt", "a") as file:
        file.write("\n" + ",".join(map(str, raices)))

crear_fichero()
calcular_raices()