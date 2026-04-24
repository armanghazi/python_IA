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
edades = [random.randint(-7, 130) for _ in range(500)]
edades.count(-3)
edades.count(121)


# Usar filter para eliminar los valores negativos y mayores de 120

lambda num: num >= 0 and num<=120

edades_correctas = list(filter(lambda num: num >= 0 and num<=120, edades))
edades_correctas.count(-3)
edades_correctas.count(121)
len(edades_correctas)

# Usar map para sustituirlos por 120 o 0
def corrector(num):
    if num>120:
        return 120
    elif num<0:
        return 0
    else:
        return num

edades_correctas2 = list(map(corrector,edades))

edades_correctas2.count(-3)
edades_correctas2.count(121)
len(edades_correctas2)