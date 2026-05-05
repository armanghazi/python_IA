from datetime import datetime


class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2

        self.trabajando = False
        self.fichajes_entrada = []
        self.fichajes_salida = []

        self.sueldo_hora = 20
        self.dietas = 0

    def ficha(self):
        self.trabajando = not self.trabajando

        if self.trabajando:
            self.fichajes_entrada.append(datetime.now())
        else:
            self.fichajes_salida.append(datetime.now())

        self.asignar_dieta()

    def asignar_dieta(self):
        
        self.dietas += 1

    def calcula_tiempo_trabajado(self):
        total = 0
        for e, s in zip(self.fichajes_entrada, self.fichajes_salida):
            total += (s - e).total_seconds()
        return total

    def calcula_sueldo(self):
        horas = self.calcula_tiempo_trabajado() / 3600
        return horas * self.sueldo_hora + self.dietas

    def __str__(self):
        return f"{self.nombre} {self.apellido1} | Sueldo total: {self.calcula_sueldo():.2f}€"


# ---------------------
# DIRECTIVO
# ---------------------
class Directivo(Persona):
    def __init__(self, nombre, apellido1, apellido2, coche_empresa):
        super().__init__(nombre, apellido1, apellido2)  
        self.coche_empresa = coche_empresa

    def asignar_dieta(self):
        
        self.dietas += 20


# ---------------------
# OFICINISTA
# ---------------------
class Oficinista(Persona):
    def __init__(self, nombre, apellido1, apellido2, bonus):
        super().__init__(nombre, apellido1, apellido2)
        self.bonus = bonus

    def calcula_sueldo(self):
        base = super().calcula_sueldo()
        return base + self.bonus


# ---------------------
# PEON
# ---------------------
class Peon(Persona):
    def __init__(self, nombre, apellido1, apellido2, guardias):
        super().__init__(nombre, apellido1, apellido2)
        self.guardias = guardias

    def asignar_dieta(self):
      
        hora_actual = datetime.now().hour
        if hora_actual >= 22 or hora_actual < 6:
            self.dietas += 10
        else:
            self.dietas += 1


# ---------------------
# test
# ---------------------

d = Directivo("Juan", "Perez", "Lopez", "BMW")
o = Oficinista("Ana", "Garcia", "Lopez", 100)
p = Peon("Luis", "Martinez", "Diaz", 3)

# fichar
d.ficha()
d.ficha()

o.ficha()
o.ficha()

p.ficha()
p.ficha()

print(d)
print(o)
print(p)