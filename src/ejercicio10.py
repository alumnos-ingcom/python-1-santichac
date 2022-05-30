################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una
palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda
que de izquierda a derecha.
"""

def es_palindromo(texto):
    """
    Esta función verifica si una palabra es palindromo o no.
    """
    texto = texto.lower()
    texto = texto.replace(' ', '')
    longitud = len(texto)
    if longitud % 2 == 0:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2:]
    else:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2 + 1:]

    return izquierda == derecha[::-1]

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    frase_palabra = input('Ingrese una frase o una palabra:')
    print(es_palindromo(frase_palabra))

if __name__ == "__main__":
    principal()

