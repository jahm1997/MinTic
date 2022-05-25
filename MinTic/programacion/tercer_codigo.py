# código que permite cargar dos listas y comparar el elemento 2 de cada una
from random import random


primeralista=[1,2,3,4,5,6,7,8,9]
segundalista=[0,4,7,9,2]
terceralista=[1,2,67,8,9,4,3]
cuartalista=[0,2,5,76,34,78,234]


def comparando_lista(lista1,lista2):

    Element1 = lista1[random.choice(lista1)]
    Element2 = lista2[random.choice(lista2)]


    if  Element1 == Element2:
        return f' "la lista1 su concuerda la posicion 1 de la lista2" '
    else:
        return f' "Estas Errado" '

print(comparando_lista(primeralista,terceralista))