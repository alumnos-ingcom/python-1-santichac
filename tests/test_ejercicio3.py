from src.ejercicio3 import compara

def test_compara_positivo():
    """
    Esta test evalua que la función compara() ingresando un valor y
    revisando que el resultado sea el esperado.
    """
    numero = 9 
    otro_numero = 3
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), ' '
    assert resultado == '1', 'El resultado no es el esperado.'

def test_compara_negativo():
    """
    Esta test evalua que la función compara() ingresando un valor y
    revisando que el resultado sea el esperado.
    """
    numero = 3
    otro_numero = 9
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), ' '
    assert resultado == '-1', 'El resultado no es el esperado.'

def test_compara_cero():
    """
    Esta test evalua que la función compara() ingresando un valor y
    revisando que el resultado sea el esperado.
    """
    numero = 16
    otro_numero = 16
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, str), ' '
    assert resultado == '0', 'El resultado no es el esperado.'