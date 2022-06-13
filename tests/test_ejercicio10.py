################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio10 import es_palindromo

"""
Este es el test correspondiente al archivo 'ejercicio10.py'
"""

def test_es_palindromo():
    """
    Este test evalua la función es_palindromo() ingresando una palabra
    y revisando que sea palindromo.
    """
    texto = 'neuquen'
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), 'El resultado de la función debe ser de tipo booleano o sea, True o False. En este caso True.'
    assert resultado == True, 'El resultado no es el esperado.'

def test_no_es_palindromo():
    """
    Este test evalua la función es_palindromo() ingresando una palabra
    y revisando que sea no palindromo.
    """
    texto = 'rio negro'
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), 'El resultado de la función debe ser de tipo booleano o sea, True o False. En este caso False.'
    assert resultado == False, 'El resultado no es el esperado.'
