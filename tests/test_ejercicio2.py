################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import signo

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_signo_positivo():
    """
    Este test evalua la función signo() ingresando un valor 
    revisando que el resultado sea el numero esperado
    """
    numero = 9.3
    resultado = signo(numero)
    assert isinstance(resultado, int), 'El resultado debe ser de tipo float o sea, que sea un número con coma.'
    assert resultado == 1, 'El resultado no es el esperado'

def test_signo_negativo():
    """
    Este test evalua la función signo() ingresando un valor 
    revisando que el resultado sea el numero esperado
    """
    numero = -9.3
    resultado = signo(numero)
    assert isinstance(resultado, int), 'El resultado debe ser de tipo float o sea, que sea un número con coma.'
    assert resultado == -1, 'El resultado no es el esperado.'

def test_signo_cero():
    """
    Este test evalua la función signo() ingresando un valor 
    revisando que el resultado sea el numero esperado
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int),  'El resultado debe ser de tipo float o sea, que sea un número con coma.'
    assert resultado == 0, 'El resultado no es el esperado.'
