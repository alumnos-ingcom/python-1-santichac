################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número
entero es multiplo de otro, utilizando sumas y restas.
"""

def es_multiplo(numero, multiplo):
    """
    Esta función verifica si un numero entero es
    multiplo de otro
    """
    while numero > 0:
        numero = numero - multiplo
    if numero == 0:
        devolucion = True
    else:
        devolucion = False
    return devolucion

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: '))
    multiplo = int(input('Ingrese el numero que quiera saber si es multiplo: '))
    print(es_multiplo(numero, multiplo))

if __name__ == "__main__":
    principal()


