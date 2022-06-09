from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

"""
Este es el test correspondiente al archivo 'ejercicio7.py'
"""

def test_sexadecimal_a_decimal():
    """
    Este test evalua la función sexadecimal_a_decimal() ingresando una cantidad
    de grados, 
    """
    horas = 13
    minutos = 45
    segundos = 300
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), ''
    assert resultado == 49800, ''

def test_decimal_a_sexadecimal():
    numero = 49800
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), ' '
    assert resultado == (13, 50, 0), ' '
