#############
# Ejercicio #
#___________#

# Crear la clase coche que incluya los atributos 
# "marca", "modelo", "longitud" y "precio"


# Crear objetos de la clase coche
# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos

# Atribuirles métodos que permitan imprimir en la pantalla:
# Un mensaje al borrar el objeto
#del(coche1)

# un valor de longitud
# len(coche1)

# un valor al hacer print()
# print(coche2)


# Crear métodos que permitan comparar los coches por el precio:
# if coche1 > coche2:
#   pass

# Crear la clase coche

    

# Crear objetos de la clase coche
# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos
# coche1 = Coche("Renault", "Megane", 3.5, 3000)
# coche2 = Coche("BMW", "530", 3.7, 4500)

# Atribuirles métodos que permitan imprimir en la pantalla:
# Un mensaje al borrar el objeto
# del(coche1)
# un valor de longitud
# len(coche2)
# un valor al hacer print()
# print(coche2)

# coche2.saludar()

# coche1 < coche2

# coche1.maximo(coche2)

# coche2
# max(coche1, coche2)

# lista_coches = [coche2, coche1]
# print(lista_coches)

# lista_coches.sort()
# print(lista_coches)



# Crear la clase coche que incluya los atributos 
# "marca", "modelo", "longitud" y "precio"
class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio

    # Mensaje al borrar el objeto
    def __del__(self):
        print(f"Se ha eliminado el coche {self.marca} {self.modelo}")

    # Para usar len()
    def __len__(self):
        return int(self.longitud)

    # Para print()
    def __str__(self):
        return f"{self.marca} {self.modelo} de  {self.precio}€"

    # Método extra
    def saludar(self):
        print(f"Hola, soy un {self.marca} {self.modelo}")

    # Comparaciones por precio
    def __lt__(self, otro):
        if isinstance(otro, Coche):
            return self.precio < otro.precio
        else:
            print (f"{otro} no es un coche")

    def __gt__(self, otro):
        return self.precio > otro.precio

    def __eq__(self, otro):
        return self.precio == otro.precio

    # Método que devuelve el coche más caro
    def maximo(self, otro):
        if self.precio > otro.precio:
            return self
        else:
            return otro


# Crear objetos
coche1 = Coche("Renault", "Megane", 3.5, 3000)
coche2 = Coche("BMW", "530", 3.7, 4500)

# len()
print(len(coche2))

# print()
print(coche2)

# método propio
coche2.saludar()

# comparación
print(coche1 < coche2)

# máximo con método propio
print(coche1.maximo(coche2))

# máximo con función integrada
print(max(coche1, coche2))

# lista de coches
lista_coches = [coche2, coche1]
print(lista_coches)

# ordenar lista (por precio)
lista_coches.sort()
print(lista_coches)

# borrar objeto
del coche1