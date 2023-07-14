import random

def almacenar_numeros():
    numeros = []
    for _ in range(10):
        numeros.append(random.randint(1, 100))
    print("Lista original:", numeros)
    return numeros

def numeros_no_repetidos():
    numeros = almacenar_numeros()
    numeros_no_rep = list(set(numeros))
    print("Números no repetidos:", numeros_no_rep)
    return numeros_no_rep

def ordenar_listas():
    numeros_no_rep = numeros_no_repetidos()
    lista_mayor_menor = sorted(numeros_no_rep, reverse=True)
    lista_menor_mayor = sorted(numeros_no_rep)
    print("Lista ordenada de mayor a menor:", lista_mayor_menor)
    print("Lista ordenada de menor a mayor:", lista_menor_mayor)
    return lista_mayor_menor, lista_menor_mayor

def obtener_mayor():
    lista_mayor_menor, _ = ordenar_listas()
    mayor = lista_mayor_menor[0]
    print("Mayor número de la lista:", mayor)
    return mayor


almacenar_numeros()
numeros_no_repetidos()
ordenar_listas()
obtener_mayor()