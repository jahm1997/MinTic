
from functools import reduce


def mayor_A_5(elemento):
    return elemento>5
tupla = (5,6,8,3,7,32,5,10,8,5,11,4,53,93)

resultado = tuple(filter(mayor_A_5,tupla))
resultado = len(resultado)
print(resultado)

lista = [4,9,8,3,2]
acumulador = 0
for i in lista:
    acumulador += i
print(acumulador)

def fun_acum(acumu,lemento):
    return acumu + lemento

entonces = reduce(fun_acum,lista)
print(entonces)

# desde aqui es any y all

uids = ["B1CD102354","B1CDEF2354"]
for uid in uids:
    condic = []
    #lertas mayusculas del alfabeto ingles
    condic.append(len(list(filter(lambda x: x.isupper(), list(uid))))>=2)
    condic.append(len(list(filter(lambda x: x.isdigit(), list(uid))))>=3)
    condic.append(len(list(filter(lambda x: not (x.isalnum()), list(uid))))>=0)
    condic.append(len(uid) == len(set(uid)))
    condic.append(len(uid) == 10)
    print ("valid") if all(condic) else print ("invalido")


print (condic)
# aqui finaliza any y all