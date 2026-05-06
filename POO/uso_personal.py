from POO.personal import Persona

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
print(secretario.calcula_tiempo_trabajado())
secretario.dietas

print(secretario.calcula_sueldo())
secretario.asigna_sueldo()