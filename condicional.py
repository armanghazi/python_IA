#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:45:24 2023

@author: Aitor Donado
"""

# 1. Crear una lista con 10 elementos numéricos.

lista = [12, 8, 21, 6, 15, 3, 9, 18, 5, 10]
######################################

# 2. Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que
# muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.

lista[2] > lista[6] 

tercero = lista[2]
septimo = lista[6]
if tercero > septimo:
    print(f"El tercer elemento ({tercero}) es mayor que el séptimo ({septimo})")
else:
    print(f"El tercer elemento ({tercero}) es menor que el séptimo ({septimo})")
######################################

# 3. Invertir el orden de la lista y realizar la misma comprobación.

lista.reverse()

tercero_reverse = lista[2]
septimo_reverse = lista[6]

if tercero_reverse > septimo_reverse:
    print(f"(Invertida) El tercer elemento ({tercero_reverse}) es mayor que el séptimo ({septimo_reverse})")
else:
    print(f"(Invertida) El tercer elemento ({tercero_reverse}) es menor que el séptimo ({septimo_reverse})")

######################################

# 4. Añadir la posibilidad de que sea igual.

if tercero > septimo:
    print(f"El tercer elemento ({tercero}) es mayor que el séptimo ({septimo})")
elif tercero < septimo:
    print(f"El tercer elemento ({tercero}) es menor que el séptimo ({septimo})")
else:
    print(f"El tercer elemento ({tercero}) es igual al séptimo ({septimo})")

######################################


# 5. Transformar el séptimo número para que se satisfaga la igualdad.

lista[6] = lista[2]

######################################


# 6. Realizar la comprobación.

tercero = lista[2]
septimo = lista[6]
if tercero > septimo:
    print(f"El tercer elemento ({tercero}) es mayor que el séptimo ({septimo})")
elif tercero < septimo:
    print(f"El tercer elemento ({tercero}) es menor que el séptimo ({septimo})")
else:
    print(f"El tercer elemento ({tercero}) es igual al séptimo ({septimo})")

######################################