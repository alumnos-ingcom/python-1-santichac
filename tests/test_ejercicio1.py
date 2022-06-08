from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_convertir_a_fahrenheit_positivos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    centigrados = 31
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == 87.8, "El resultado no es el esperado"
    
def test_convertir_a_fahrenheit_negativos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    centigrados = -10
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == 14, "El resultado no es el esperado"

def test_convertir_a_centigrados_positivos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    fahrenheit = 87.8
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == 31, "El resultado no es el esperado"
    
def test_convertir_a_centigrados_negativos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    fahrenheit = -5
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado de la conversión debe ser de tipo float o sea, que sea un número con coma."
    assert resultado == -20.555555555555557, "El resultado no es el esperado"
