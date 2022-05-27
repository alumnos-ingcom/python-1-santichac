################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero
indicado es Primo.
"""

def es_primo(numero):
    """
    Esta función indica si un número es primo o no
    """
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for primo_a in range(2, numero):
            if numero % primo_a == 0:
                return False
        return True

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un numero:'))
    resultado = es_primo(numero)

    if resultado is True:
        print('El número es primo')
    else:
        print('El número no es primo')


if __name__ == "__main__":
    principal()
