################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_suma_lenta_positivos():
    """
    Este test evalua la función suma_lenta() ingresando dos valores
    y revisando que el resultado sea el npumero esperado de tipo int positivo
    """
    numero = 16
    otro_numero = 9
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), 'El resultado de la función debe ser de tipo int y positivo o sea, tiene que ser entero y mayor que 0'
    assert resultado == 25, 'El resultado no es el esperado.'

def test_suma_lenta_uno_negativo():
    """
    Este test evalua la función suma_lenta() ingresando dos valores
    y revisando que el resultado sea el npumero esperado de tipo int negativo o positivo
    """
    numero = 3
    otro_numero = -9
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), 'El resultado de la función debe ser de tipo int y positivo o negativo o sea, tiene que ser entero y mayor, menor o igual a 0'
    assert resultado == -6, 'El resultado no es el esperado.'

def test_suma_lenta_ambos_negativos():
    """
    Este test evalua la función suma_lenta() ingresando dos valores
    y revisando que el resultado sea el npumero esperado de tipo int negativo
    """
    numero = -16
    otro_numero = -3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), 'El resultado de la función debe ser de tipo int y negativo o sea, tiene que ser entero y menor que 0'
    assert resultado == -19, 'El resultado no es el esperado.'
