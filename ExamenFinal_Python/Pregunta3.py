import time

def medir_tiempo(func):
    def sub(*args, **args2):
        start_time = time.time()
        resultado = func(*args, **args2)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Tiempo de ejecución:", execution_time, "segundos")
        return resultado
    return sub

def multiplicacion(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# Uso del decorador
multiplicacion_medida = medir_tiempo(multiplicacion)

# Ejemplos de uso
print(multiplicacion_medida(2, 3, 4))
print(multiplicacion_medida(5, 10))
print(multiplicacion_medida(1, 2, 3, 4, 5))