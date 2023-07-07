def ingresar_datos():
    while True:
        try:
            dato1 = int(input("Ingrese el primer dato: "))
            dato2 = int(input("Ingrese el segundo dato: "))
            return dato1, dato2
        except ValueError:
            print("Error: Ingrese solo números enteros. Intente nuevamente.")

def division_entre_cero(a, b):
    while True:
        try:
            resultado = a / b
            return resultado
        except ZeroDivisionError:
            print("No se puede dividir entre cero. Intente nuevamente UwU.")
            a, b = ingresar_datos()

def evaluar_suma(dato1, dato2):
    while True:
        try:
            suma = dato1 + dato2
            if suma < 100:
                return suma
            else:
                raise ValueError
        except ValueError:
            print("La suma debe ser menor a 100. Intente nuevamente UwU.")
            dato1, dato2 = ingresar_datos()


dato1, dato2 = ingresar_datos()

# División
resultado_division = division_entre_cero(dato1, dato2)
print("Resultado de la división:", resultado_division)

# Suma
resultado_evaluacion = evaluar_suma(dato1, dato2)
print("Resultado de la suma evaluada:", resultado_evaluacion)