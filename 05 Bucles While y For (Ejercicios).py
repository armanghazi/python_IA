# 1. Contador de números pares e impares:
"""
Escribe un programa que utilice un bucle for o while para contar y mostrar 
la cantidad de números pares e impares en un rango específico, 
por ejemplo, del 1 al 100.
"""
pares = 0
impares = 0
for i in range(1, 101):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Hay {pares} numeros pares y {impares} numeros impares")

######################################


# 2. Suma de números primos:
"""
Crea un programa que solicite al usuario un número y utilice un bucle 
while para sumar todos los números primos menores o iguales al número 
ingresado.
"""
def primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

numero = int(input("Ingresa un número: "))
sum = 0
i = 2

while i <= numero:
    if primo(i):
        sum += i
    i += 1
print(f"Los números primos menores o iguales a {numero} son:")

print("La suma de los números primos es:", sum)

######################################

numero = int(input("Ingresa un número: "))
suma_primos = 0

print(f"Los números primos menores o iguales a {numero} son:")

for n in range(2, numero + 1):
    es_primo = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        print(n, end=" ")
        suma_primos += n

print("\nLa suma de los números primos es:", suma_primos)



# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""
5

######################################


# 4. Generador de patrones:
"""
Escribe un programa que solicite al usuario un número y utilice 
un bucle for o while para generar patrones como el siguiente, donde 
el número ingresado determine la cantidad de filas:
"""
1
22
333
4444
55555

# 5. Adivina el número:
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

randint(0, 100)












