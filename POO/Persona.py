# Crear un método que asigne una dieta de transporte de un euro cada vez que una persona fiche
# Modificar el método que calcula el sueldo para que añada la dieta de transporte.

class Persona:
    pass

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.calcula_tiempo_trabajado()
secretario.dietas

secretario.calcula_sueldo()
secretario.asigna_sueldo()





from datetime import datetime

class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2

        self.trabajando = False
        self.ubicacion = "Rentería"

        self.fichajes_entrada = []
        self.fichajes_salida = []

        self.sueldo_hora = 20
        self.dietas = 0   

    def presentarse(self):
        print(f'Hola, soy {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando

        if self.trabajando:
            self.fichajes_entrada.append(datetime.now())
        else:
            self.fichajes_salida.append(datetime.now())
 
      
        self.asignar_dieta()

    def asignar_dieta(self):
        self.dietas += 1
        print(f"Dieta añadida. Total dietas: {self.dietas}€")

    def calcula_tiempo_trabajado(self):
        if not self.fichajes_entrada or not self.fichajes_salida:
            return 0

        tiempo_total = 0
        for entrada, salida in zip(self.fichajes_entrada, self.fichajes_salida):
            tiempo_total += (salida - entrada).total_seconds()

        return tiempo_total

    def asigna_sueldo(self):
        cambio = float(input("Cuánto quieres variar el sueldo: "))
        self.sueldo_hora += cambio
        print(f"Nuevo sueldo: {self.sueldo_hora}€/h")

    def calcula_sueldo(self):
        horas = self.calcula_tiempo_trabajado() / 3600
        sueldo = horas * self.sueldo_hora

       
        sueldo_total = sueldo + self.dietas

        return sueldo_total


# -----------------------
# USO
# -----------------------

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.ficha()

print("Tiempo trabajado:", secretario.calcula_tiempo_trabajado())
print("Dietas:", secretario.dietas)

print("Sueldo total:", secretario.calcula_sueldo())

secretario.asigna_sueldo()