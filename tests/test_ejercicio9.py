from src.ejercicio9 import factores_primos

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_factores_primos():
    """
    Este test evalua la función factores_primos() ingresando un valor y
    revisando que el resultado sean los factores primos de ese valor
    """
    numero = 3916
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), 'El resultado de la función debe ser de tipo tupla o sea, tiene que mostrar los factores primos así (1, 2, 3)'
    assert resultado == (2, 2, 11, 89), 'El resultado no es el esperado.'
