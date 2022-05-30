################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres
variables de tipo entero retorne una tupla
con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función recibe 3 valores y los ordena de mayor a menor
    """
    ordenados_a = [ ]
    if uno > dos and uno > tres:
        ordenados_a.append(uno)
        if dos > tres:
            ordenados_a.append(dos)
            ordenados_a.append(tres)
        else:
            ordenados_a.append(tres)
            ordenados_a.append(dos)
    elif dos > uno and dos > tres:
        ordenados_a.append(dos)
        if uno > tres:
            ordenados_a.append(uno)
            ordenados_a.append(tres)
        else:
            ordenados_a.append(tres)
            ordenados_a.append(uno)
    elif tres > uno and tres > dos:
        ordenados_a.append(tres)
        if uno > dos:
            ordenados_a.append(uno)
            ordenados_a.append(dos)
        else:
            ordenados_a.append(dos)
            ordenados_a.append(uno)
    return tuple(ordenados_a)

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función recibe 3 valores y los ordena de menor a mayor
    """
    ordenados_b = [ ]
    if uno < dos and uno < tres:
        ordenados_b.append(uno)
        if dos < tres:
            ordenados_b.append(dos)
            ordenados_b.append(tres)
        else:
            ordenados_b.append(tres)
            ordenados_b.append(dos)
    elif dos < uno and dos < tres:
        ordenados_b.append(dos)
        if uno < tres:
            ordenados_b.append(uno)
            ordenados_b.append(tres)
        else:
            ordenados_b.append(tres)
            ordenados_b.append(uno)
    elif tres < uno and tres < dos:
        ordenados_b.append(tres)
        if uno < dos:
            ordenados_b.append(uno)
            ordenados_b.append(dos)
        else:
            ordenados_b.append(dos)
            ordenados_b.append(uno)
    return tuple(ordenados_b)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    uno = int(input('Ingrese el primer numero:'))
    dos = int(input('Ingrese el segundo numero:'))
    tres = int(input('Ingrese el tercer numero:'))
    print('De mayor a menor es:', ordenar_mayor_a_menor(uno, dos, tres))
    print('De menor a mayor es:', ordenar_menor_a_mayor(uno, dos, tres))

if __name__ == "__main__":
    principal()

