#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

###################
# Encapsulamiento #
###################

"""Al utilizar el encapsulamiento, se evita que los atributos privados de una clase sean 
manipulados directamente desde fuera de la clase, lo que garantiza la integridad de los 
datos internos de la clase. """


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor que 120")
        self.__edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.__edad} años')


"""El atributo nombre es público, mientras que el atributo __edad es privado. 
Además, la clase tiene dos métodos públicos: get_edad() y set_edad(). 
El método get_edad() devuelve el valor del atributo privado __edad, 
mientras que el método set_edad() establece el valor del atributo privado __edad 
después de validar que el valor de edad es válido."""

vigilante = Persona("Pedro", 50)
vigilante.__edad

vigilante.__edad = 25

dir(vigilante)
vigilante.saludar()

vigilante.set_edad(151)
vigilante.get_edad()

vigilante.__edad

vigilante.saludar()

# Decoradores property y setter
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
    
    @property
    def edad(self):
        if input("Escribe password: ") == "password":
            return self.__edad
        else:
            return "No te doy la información"


    @edad.setter
    def edad(self, edad):    
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor que 120")
        elif input("Escribe password: ") == "password": 
            self.__edad = edad


    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.__edad} años')


vigilante = Persona("Pedro", 50)
vigilante.edad
vigilante.edad = 130
vigilante.edad = -3
vigilante.edad = 51
vigilante.edad

vigilante.saludar()

class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.__ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        self.trabajando = not self.trabajando

    def sale_de_viaje(self, nueva_ubicacion):
        print(f"{self.__ubicacion} -----> {nueva_ubicacion}")
        self.__ubicacion = nueva_ubicacion
        print(self.__esta_en())

    def __esta_en(self):
        return self.__ubicacion



director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

director.presentarse()
secretario.presentarse()
secretario.sale_de_viaje("Bilbao")
secretario.__esta_en()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
# print(f"¿Dónde está el director? {director.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el director? {director.esta_en()}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
# print(f"¿Dónde está el secretario? {secretario.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el secretario? {secretario.__esta_en()}")

# director.__ubicacion = "Oyarzun" # Ya no funciona
director.sale_de_viaje("Oyarzun")

director.__ubicacion = "Bilbao"
dir(director)
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
# print(f"¿Dónde está el director? {director.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el director? {director.esta_en()}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
# print(f"¿Dónde está el secretario? {secretario.__ubicacion}") # Ya no funciona
print(f"¿Dónde está el secretario? {secretario.esta_en()}")


# También pueden encapsularse métodos que no quiero que se activen desde fuera
# (Seguramente porque requieren de operaciones previas)

#############
# Ejercicio #
#___________#

# Vamos a encapsular "trabajando", "sueldo_hora"... en el ejercicio del personal


class Persona:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora):
        # Atributos Públicos
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        
        # Atributos Privados (Encapsulados)
        self.__trabajando = False
        self.__sueldo_hora = sueldo_hora
        self.__ubicacion = "Rentería"

    # --- Encapsulamiento de 'trabajando' ---
    @property
    def trabajando(self):
        """Getter para el estado laboral"""
        return self.__trabajando

    @trabajando.setter
    def trabajando(self, estado):
        """Setter con validación de tipo booleano"""
        if isinstance(estado, bool):
            self.__trabajando = estado
        else:
            print("Error: El estado de trabajo debe ser True o False")

    # --- Encapsulamiento de 'sueldo_hora' ---
    @property
    def sueldo_hora(self):
        """Getter para el sueldo"""
        return self.__sueldo_hora

    @sueldo_hora.setter
    def sueldo_hora(self, valor):
        """Setter con validación de rango (similar a la edad)"""
        if valor < 0:
            raise ValueError("El sueldo no puede ser negativo")[cite: 1]
        self.__sueldo_hora = valor

    # Métodos de comportamiento
    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        """Cambia el estado de trabajo de forma interna"""
        self.__trabajando = not self.__trabajando

    def sale_de_viaje(self, nueva_ubicacion):
        print(f"{self.__ubicacion} -----> {nueva_ubicacion}")
        self.__ubicacion = nueva_ubicacion

    def donde_esta(self):
        return self.__ubicacion

# --- Prueba del código ---

director = Persona('Juan', 'Pérez', 'López', 50.0)

# Acceso a través de los decoradores property
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
director.trabajando = True  # Usa el setter
print(f"Sueldo actual: {director.sueldo_hora}€")

# Intentar modificar con un valor inválido
try:
    director.sueldo_hora = -10
except ValueError as e:
    print(f"Error detectado: {e}")[cite: 1]

# El acceso directo a __trabajando fallaría o no afectaría al atributo real
# director.__trabajando = "No quiero trabajar" # Esto crearía un atributo nuevo, no el privado

from abc import ABC, abstractmethod

# Clase Abstracta: No se puede instanciar directamente
class Empleado(ABC):
    def __init__(self, nombre, apellido, sueldo_hora):
        self.nombre = nombre
        self.apellido = apellido
        # Atributos encapsulados (Privados)
        self.__sueldo_hora = sueldo_hora
        self.__trabajando = False

    # --- Encapsulamiento de sueldo_hora ---
    @property
    def sueldo_hora(self):
        return self.__sueldo_hora

    @sueldo_hora.setter
    def sueldo_hora(self, valor):
        if valor < 0:
            raise ValueError("El sueldo no puede ser negativo")[cite: 1]
        self.__sueldo_hora = valor

    # --- Encapsulamiento de trabajando ---
    @property
    def trabajando(self):
        return self.__trabajando

    @trabajando.setter
    def trabajando(self, estado):
        if isinstance(estado, bool):
            self.__trabajando = estado

    # Método abstracto: obliga a las subclases a definir su propia lógica
    @abstractmethod
    def realizar_tarea(self):
        pass

    def fichar(self):
        self.__trabajando = not self.__trabajando
        estado = "entrando a" if self.__trabajando else "saliendo de"
        print(f"{self.nombre} está {estado} trabajar.")

# --- Subclases específicas ---

class Directivo(Empleado):
    def realizar_tarea(self):
        return f"{self.nombre} está supervisando la estrategia."

class Oficinista(Empleado):
    def realizar_tarea(self):
        return f"{self.nombre} está procesando documentos."

class Peon(Empleado):
    def realizar_tarea(self):
        return f"{self.nombre} está operando maquinaria."

# --- Pruebas de instanciación ---

# jefe = Empleado("Carlos", "García", 20) 
# ^ Esto lanzaría un error: Can't instantiate abstract class Empleado

director = Directivo("Elena", "Sanz", 60.5)
administrativo = Oficinista("Luis", "Pérez", 15.0)
operario = Peon("Mikel", "Etxeberria", 12.0)

# Uso de los atributos encapsulados
director.fichar()
print(f"Sueldo de {director.nombre}: {director.sueldo_hora}€")[cite: 1]
print(operario.realizar_tarea())