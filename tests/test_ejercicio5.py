################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import division_lenta

"""
Este es el test correspondiente al archivo 'ejercicio5.py'
"""

def test_division_lenta():
    """
    Este test evalua la función division_lenta() ingresando dos valores y 
    revisando que el resto y el cociente den bien.
    """
    dividendo = 16
    divisor = 9
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar 1 de cociente y 7 de resto.'
    assert resultado == (f'El cociente es {1} y el resto es {7}'), 'El resultado no es el esperado.'

def test_division_lenta_primero_negativo():
    """
    Este test evalua la función division_lenta() ingresando dos valores y 
    revisando que el resto y el cociente den bien.
    """
    dividendo = -81
    divisor = 9
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar -9 de cociente y 0 de resto.'
    assert resultado == (f'El cociente es {-9} y el resto es {0}'), 'El resultado no es el esperado.'

def test_division_lenta_ambos_negativos():
    """
    Este test evalua la función division_lenta() ingresando dos valores y 
    revisando que el resto y el cociente den bien.
    """
    dividendo = -17
    divisor = -6
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar 2 de cociente y -5 de resto.'
    assert resultado == (f'El cociente es {2} y el resto es {-5}'), 'El resultado no es el esperado.'

def test_division_lenta_segundo_negativo():
    """
    Este test evalua la función division_lenta() ingresando dos valores y 
    revisando que el resto y el cociente den bien.
    """
    dividendo = 52
    divisor = -3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar -17 de cociente y 1 de resto.'
    assert resultado == (f'El cociente es {-17} y el resto es {1}'), 'El resultado no es el esperado.'
    