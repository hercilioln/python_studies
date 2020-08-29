import random

def selectionSort(lista):
    n = len(lista)
    for j in range(n-1):
        indicemenor = j
        for i in range(j, n):
            if lista[i] < lista[indicemenor]:
               indicemenor = i
        if lista[j] > lista[indicemenor]:
            aux = lista[j]
            lista[j] = lista[indicemenor]
            lista[indicemenor] = aux


lista = random.sample(range(1, 50), 5)
print("\n==Lista com números aleatórios==")
print(lista)
selectionSort(lista)
print("\n==Ordenado com Selection Sort==")
print(lista)
