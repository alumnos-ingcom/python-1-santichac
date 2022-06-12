from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

"""
Este es el test correspondiente al archivo 'ejercicio7.py'
"""

def test_sexadecimal_a_decimal():
    """
    Este test evalua la función sexadecimal_a_decimal() ingresando una cantidad
    de grados, minutos y segundos y revisando que el resultado sea la cantidad de segundos esperada.
    """
    horas = 13
    minutos = 45
    segundos = 300
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), 'El resultado de la conversión debe ser de tipo int o sea, un número entero.'
    assert resultado == 49800, 'El resultado no es el esperado'

def test_decimal_a_sexadecimal():
    """
    Este test evalua la funcion decimal_a_sexadecimal() ingresando un valor 
    de segundos y revisando que el resultado sea una tupla con grados, minutos y segundos.
    """
    numero = 49800
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), 'El resultado de la conversión debe ser de tipo tuple o sea, tiene que ser asi: (grados, minutos, segundos).'
    assert resultado == (13, 50, 0), 'El resultado no es el esperado.'
