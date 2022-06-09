from src.ejercicio8 import es_primo

"""
Este es el test correspondiente al archivo 'ejercicio8.py'
"""

def test_es_primo():
    """
    Este test evalua la función es_primo() ingresando un valor y
    revisando que el resultado sea el número esperado y de tipo bool
    """
    numero = 23
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), 'El resultado esperado debe ser de tipo booleano o sea, True o False.'
    assert resultado == True, 'El resultado no es el esperado.'

def test_no_es_primo():
    """
    Este test evalua la función es_primo() ingresando un valor y
    revisando que el resultado sea el número esperado y de tipo bool
    """
    numero = 16
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), 'El resultado esperado debe ser de tipo booleano o sea, True o False.'
    assert resultado == False, 'El resultado no es el esperado.'
