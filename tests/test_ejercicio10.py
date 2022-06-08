from src.ejercicio10 import es_palindromo

"""
Este es el test correspondiente al archivo 'ejercicio10.py'
"""

def test_es_palindromo():
    texto = 'neuquen'
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), 'El resultado de la función debe ser de tipo booleano o sea, True o False.'
    assert resultado == True, 'El resultado no es el esperado.'
