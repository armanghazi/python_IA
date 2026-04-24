# Crear una lista con los números de 0 al 100.
# Desordenarla aleatoriamente

numeros = list(range(0, 101))
random.shuffle(numeros)
print(numeros)

# Dividirlos entre tres con map y una función lambda.



# Filtrar del resultado anterior los que tienen parte decimal con una función lambda.

import random

numeros = list(range(0, 101))
random.shuffle(numeros)

divididos = list(map(lambda x: x / 3, numeros))
con_decimal = list(filter(lambda x: x % 1 != 0, divididos))

print(con_decimal)

    




#___________#
# Ejercicio #
#-----------#
# Creamos una lista de edades que por error contiene números negativos y excesivos
import random
edades = [random.randint(-7, 130) for i in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores negativos y mayores de 120




# Usar map para sustituirlos por 120 o 0

