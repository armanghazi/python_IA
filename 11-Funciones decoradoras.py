
#Ejercicio1: Decorador de Validación de Parámetros
"""
Crea un decorador llamado validar_parametros que tome una función y verifique si los parámetros 
cumplen ciertas condiciones antes de llamar a la función. 

Por ejemplo, puedes implementar una validación que asegure que los números ingresados son positivos.
"""
def valida_num_entrada(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"El argumento por posición {arg} no es un número")
        for clave, valor in kwargs.items():
            if not isinstance(valor, (int, float)):
                raise TypeError(f"El argumento por clave {clave} = {valor} no es un número")
        return func(*args, **kwargs)
    return wrapper

@valida_num_entrada
def evaluar_cuadratica(a, b, c, x):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    solucion = a*x*x+b*x+c
    return solucion

evaluar_cuadratica(3, 2, c="5", x=4)


#Ejercicio 2: Decorador para Logs
"""
Implementa un decorador llamado registro que registre información sobre la llamada a la función, 
como el nombre de la función, los argumentos y el resultado. Imprime esta información en la consola 
cada vez que la función decorada se ejecuta.
"""

def registro(func):
    def wrapper(*args, **kwargs):
        salida = func(*args, **kwargs)
        print(f"La función {func.__name__} devuelve {salida} para las entradas:")
        for arg in args:
            print(f"    {arg}")
        for clave, valor in kwargs.items():
            print(f"   {clave} = {valor}")
        return salida
    return wrapper

@valida_num_entrada
@registro
def evaluar_cuadratica(a, b, c, x):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    solucion = a*x*x+b*x+c
    return solucion


evaluar_cuadratica(3, 2, c=5, x=4)