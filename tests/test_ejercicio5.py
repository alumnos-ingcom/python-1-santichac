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
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar el cociente y el resto correcto de la división.'
    assert resultado == (f'El cociente es {1} y el resto es {7}'), 'El resultado no es el esperado.'

def test_division_lenta_resto_cero():
    """
    Este test evalua la función division_lenta() ingresando dos valores y 
    revisando que el resto y el cociente den bien.
    """
    dividendo = 81
    divisor = 9
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), 'El resultado de la división lenta debe dar el cociente y el resto correcto de la división.'
    assert resultado == (f'El cociente es {9} y el resto es {0}'), 'El resultado no es el esperado.'
