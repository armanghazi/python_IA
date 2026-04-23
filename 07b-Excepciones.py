# Ejercicio #
#-----------#
# 1. Crear una función que genere una excepción de tipo "ValueError" si el usuario
# introduce una edad por consola que sea negativa o mayor de 120 años.

def validar_edad(edad):
    edad = int(edad)  # Aquí puede fallar si no es número
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
    return edad




# Lo mismo pero tratando el error de que lo introducido no sea un dígito

def validar_edad(edad):
    if not edad.isdigit():
        raise ValueError("La edad debe ser un número entero.")
    edad = int(edad)
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
    return edad

# A continuación, un bucle infinito "while True" que pida la edad y trate el error
# generado por la función. El bucle parará cuando la edad sea correcta.


while True:
    edad_usuario = input("Introduce tu edad: ")

    try:
        edad_valida = validar_edad(edad_usuario)
        print(f"Edad correcta: {edad_valida}")
        break  # Salimos del bucle si todo va bien

    except ValueError as e:
        print("Error:", e)

    except Exception:
        print("Error: Debes introducir un número entero.")



#__________#
# Solución #