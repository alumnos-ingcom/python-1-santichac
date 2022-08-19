################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_convertir_a_fahrenheit_positivos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    centigrados = 9
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == 48.2, "El resultado no es el esperado"
    
def test_convertir_a_fahrenheit_negativos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    centigrados = -16
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == 3.1999999999999993, "El resultado no es el esperado"

def test_convertir_a_centigrados_positivos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    fahrenheit = 10
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == -12.222222222222221, "El resultado no es el esperado"
    
def test_convertir_a_centigrados_negativos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    fahrenheit = -3
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == -19.444444444444443, "El resultado no es el esperado"
