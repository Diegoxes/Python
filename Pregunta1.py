from datetime import datetime

class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        self.nacionalidad = "peruana"

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Error: La edad debe ser un número entero. Intente nuevamente.")

    def cumpleanios(self):
        self.edad += 1

    def obtener_fecha_hora_registro(self):
        fecha_hora_registro = datetime.now()
        return fecha_hora_registro.strftime("%Y-%m-%d %H:%M")

# Crear instancia de la clase Persona
persona = Persona()

# Solicitar datos de la persona
persona.solicitar_datos()

# Mostrar edad inicial
print("Edad inicial:", persona.edad)

# Incrementar edad 
persona.cumpleanios()
persona.cumpleanios()

#  edad actualizada
print("Edad actualizada:", persona.edad)

# Obtener y mostrar la fecha
fecha_hora_registro = persona.obtener_fecha_hora_registro()
print("Fecha y hora de registro:", fecha_hora_registro)