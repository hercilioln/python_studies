import random

def bubbleSort(lista):
    n = len(lista)
    for j in range (n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista [i+1] = lista[i+1], lista[i]

lista = random.sample(range(1, 50), 10)
print("\n=====Lista com números aleatórios======")
print(lista)
bubbleSort(lista)
print("\n=======Ordenado com Bubble Sort=======")
print(lista)


