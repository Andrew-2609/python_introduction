# conjunto = {1, 2, 3, 4}
# print(conjunto)
#
# conjunto.add(5)
# print(conjunto)
#
# conjunto.discard(3)
# print(conjunto)

conjuntoUm = {1, 2, 3, 4, 5}
conjuntoDois = {5, 6, 7, 8}

print("Conjunto Um: {}\nConjunto Dois: {}\n".format(conjuntoUm, conjuntoDois))

conjuntoUnido = conjuntoUm.union(conjuntoDois)
print("Conjunto de União: {}".format(conjuntoUnido))

conjuntoInterseccao = conjuntoUm.intersection(conjuntoDois)
print("Conjunto de Intersecção: {}".format(conjuntoInterseccao))

conjuntoDiferencaUm = conjuntoUm.difference(conjuntoDois)
conjuntoDiferencaDois = conjuntoDois.difference(conjuntoUm)

print("Conjunto de Diferença 1: {}\nConjunto de Diferença 2: {}".format(conjuntoDiferencaUm, conjuntoDiferencaDois))

conjuntoDiferencaSimetrica = conjuntoUm.symmetric_difference(conjuntoDois)

print("Conjunto de Diferença Simétrica: {}\n".format(conjuntoDiferencaSimetrica))

conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}

conjuntoSubsetAB = conjuntoA.issubset(conjuntoB)
conjuntoSubsetBA = conjuntoB.issubset(conjuntoA)

print("O conjunto A é um subconjunto de B? {}".format(conjuntoSubsetAB))
print("O conjunto B é um subconjunto de A? {}\n".format(conjuntoSubsetBA))

conjuntoSupersetAB = conjuntoA.issuperset(conjuntoB)
conjuntoSupersetBA = conjuntoB.issuperset(conjuntoA)

print("O conjunto A é um superconjunto de B? {}".format(conjuntoSupersetAB))
print("O conjunto B é um superconjunto de A? {}".format(conjuntoSupersetBA))

print("\nConvertendo lista em conjunto, e novamente em lista:\n")

lista = ["cachorro", "gato", "gato", "arara", "falcão", "cachorro"]

lista = list(set(lista))

print(lista)
