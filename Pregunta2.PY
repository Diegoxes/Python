class Persona:
    def __init__(self, saldo):
        self.nombre = ""
        self.edad = ""
        self.nacionalidad = "Peruana"
        self.__saldo = saldo

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

    def transferencia(self, persona_destino, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            persona_destino.__saldo += monto
            print("Transferencia realizada correctamente.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print("Saldo actual:", self.__saldo)


# Saldo inicial
persona1 = Persona(saldo=1000)
persona2 = Persona(saldo=500)

# Solicitar datos de la persona 1
persona1.solicitar_datos()

# Transferencia de persona 1 a persona 2
monto_transferencia = 300
persona1.transferencia(persona2, monto_transferencia)

# Después de la transferencia
persona1.mostrar_saldo()
persona2.mostrar_saldo()