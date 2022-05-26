################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres
variables de tipo entero retorne una tupla
con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función recibe 3 valores y los ordena de mayor a menor
    """
    uno = int(uno)
    dos = int(dos)
    tres = int(tres)
    ordenados_a = sorted([uno, dos, tres])
    ordenados_a.reverse()
    return ordenados_a

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función recibe 3 valores y los ordena de menor a mayor
    """
    uno = int(uno)
    dos = int(dos)
    tres = int(tres)
    ordenados_b = sorted([uno, dos, tres])
    return ordenados_b

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    uno = input('Ingrese el primer numero:')
    dos = input('Ingrese el segundo numero:')
    tres = input('Ingrese el tercer numero:')
    print('De mayor a menor es:', ordenar_mayor_a_menor(uno, dos, tres))
    print('De menor a mayor es:', ordenar_menor_a_mayor(uno, dos, tres))

if __name__ == "__main__":
    principal()
