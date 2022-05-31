################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con
factores primos de un numero entero positivo.
"""

def factores_primos(numero):
    """
    Esta función saca los factores primos de un número
    """
    primos = [ ]
    for primos_res in range(2, numero + 1):
        while numero % primos_res == 0:
            primos.append(primos_res)
            numero = numero / primos_res
    return tuple(primos)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número para sacar los factores primos: '))
    print ('Los factores primos de', numero, 'son:', factores_primos(numero))

if __name__ == "__main__":
    principal()

