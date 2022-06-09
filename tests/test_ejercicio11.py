from src.ejercicio11 import es_multiplo

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_es_multiplo():
    """
    Este test evalua la función es_multiplo() ingresando dos valores,
    un numero y un multiplo, revisando que sea o no sea multiplo
    con una devolución de tipo booleana, True o False.
    """
    numero = 16
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), 'El resultado de la función debe ser de tipo bool o sea, True o False.'
    assert resultado == True, 'El resultado no es el esperado.'

def test_no_es_multiplo():
    """
    Este test evalua la función es_multiplo() ingresando dos valores,
    un numero y un multiplo, revisando que sea o no sea multiplo
    con una devolución de tipo booleana, True o False.
    """
    numero = 16
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), 'El resultado de la función debe ser de tipo bool o sea, True o False.'
    assert resultado == False, 'El resultado no es el esperado.'