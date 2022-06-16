################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas,
reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def compara(numero, otro_numero):
    """
    Esta función recibe dos numero, los compara
    e indica si el primero es mayor que el segundo,
    si el primero es menor que el segundo o si
    los dos son iguales
    """

    if (numero - otro_numero) > 0:
        comparacion_num = 1
    elif (numero - otro_numero) < 0:
        comparacion_num = -1
    else:
        comparacion_num = 0
    return comparacion_num

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    numero = float(input('Ingrese el primer valor: '))
    otro_numero = float(input('Ingrese el segundo valor: '))
    resultado = compara(numero, otro_numero)
    print(resultado)

if __name__ == "__main__":
    principal()
