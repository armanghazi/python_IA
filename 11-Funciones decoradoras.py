#Ejercicio: Decorador de Validación de Parámetros
"""
Crea un decorador llamado validar_parametros que tome una función y verifique si los parámetros 
cumplen ciertas condiciones antes de llamar a la función. 

Por ejemplo, puedes implementar una validación que asegure que los números ingresados son positivos.
"""
def validar_parametros(func):
    def wrapper(*args, **kwargs):
        
        for valor in args:
            if valor < 0:
                raise ValueError("Todos los números deben ser positivos")

        
        for valor in kwargs.values():
            if valor < 0:
                raise ValueError("Todos los números deben ser positivos")

        return func(*args, **kwargs)

    return wrapper

@validar_parametros
def suma(a, b):
    return a + b

print(suma(5, 3))   
print(suma(-1, 3))  


#Ejercicio 2: Decorador para Logs
"""
Implementa un decorador llamado registro que registre información sobre la llamada a la función, 
como el nombre de la función, los argumentos y el resultado. Imprime esta información en la consola 
cada vez que la función decorada se ejecuta.
"""
def registro(func):
    def wrapper(*args, **kwargs):
        print(f"Nombre de la función: {func.__name__}")
        print(f"Argumentos posicionales: {args}")
        print(f"Argumentos nombrados: {kwargs}")

        resultado = func(*args, **kwargs)

        print(f"Resultado: {resultado}")
        print("-" * 30)

        return resultado
    return wrapper

@registro
def suma(a, b):
    return a + b

suma(-2, 3)

# Construir un decorador que compruebe que la salida de una función sea un número


def verificar_numero(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)

        if not isinstance(resultado, (int, float)):
            raise TypeError("El resultado debe ser un número")

        return resultado
    return wrapper

@verificar_numero
def dividir(a, b):
    return a / b

print(dividir(10, 2))   

@verificar_numero
def saludo():
    return "Hola"

saludo()