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
    Pre: numero es un número entero positivo.
    Post: la función devuelve los factores primos del número
    previamente ingresado, en una tupla.
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
    resultado = factores_primos(numero)
    print (f'Los factores primos de {numero} son: {resultado}')

if __name__ == "__main__":
    principal()
