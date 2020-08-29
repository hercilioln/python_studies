import random

def insertSort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista [j+1] = chave

lista = random.sample(range(1, 50), 8)
print("\n==Lista com números aleatórios==")
print(lista)
insertSort(lista)
print("\n==Ordenado com Insert Sort==")
print(lista)
