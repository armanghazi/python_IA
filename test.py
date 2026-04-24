import re

def extract_numbers(s):
    """
    Extrae números enteros y flotantes de un string.

    Args:
        s (str): El string del que extraer números.

    Returns:
        list: Una lista de números extraídos.
    """
    # Utilizamos la expresión regular para encontrar números enteros y flotantes
    numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", s)
    
    # Convertimos los números de string a float o int según corresponda
    numbers = [int(num) if '.' not in num else float(num) for num in numbers]
    
    return numbers

# Ejemplo de uso
string = "La suma de 10 y 20.5 es 30.5, pero también hay -5 y +10."
print(extract_numbers(string))  # Output: [10, 20.5, 30.5, -5, 10.0]