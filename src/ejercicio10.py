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
    Pre: texto es una palabra que ingresa el usuario y que desea
    saber si es palindromo o no.
    Post: la función devolvera True si la palabra es palindromo y False
    si no es palindromo.
    """
    texto_invertido = ""
    for l in texto:
        texto_invertido = l + texto_invertido
    if texto == texto_invertido:
        texto_es_palindromo = True
    else:
        texto_es_palindromo = False
    return texto_es_palindromo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    frase_palabra = input('Ingrese una frase o una palabra: ')
    resultado = es_palindromo(frase_palabra)
    if resultado:
        print(f'{resultado}, o sea la palabra es palindromo.')
    else:
        print(f'{resultado}, o sea la palabra no es palindromo.')

if __name__ == "__main__":
    principal()
