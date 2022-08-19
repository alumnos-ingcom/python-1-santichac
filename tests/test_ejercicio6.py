################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

"""
Este es el test del ejercicio6.py
"""

def test_ordenar_mayor_a_menor():
    """
    Esta test evalua la función ordenar_mayor_a_menor() ingresando tres valores y
    revisando que el orden sea correcto
    """
    uno = 16
    dos = 3
    tres = 9
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), 'El resultado debe ser una tupla que se ordene de mayor a menor.'
    assert resultado == (16, 9, 3), 'El resultado no es el esperado.'

def test_ordenar_menor_a_mayor():
    """
    Esta test evalua la función ordenar_menor_a_mayor() ingresando tres valores y
    revisando que el orden sea correcto
    """
    uno = 16
    dos = 3
    tres = 9
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), 'El resultado debe ser una tupla que se ordene de menor a mayor.'
    assert resultado == (3, 9, 16), 'El resultado no es el esperado.'
