import random
def bubble_sort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = random.sample(range(1, 50), 10)
bubble_sort(lista)
print(lista)

import random
def selection_sort(lista):
   for preencher in range(len(lista)-1,0,-1):
       posicaoMaior=0
       for localizacao in range(1,preencher+1):
           if lista[localizacao]>lista[posicaoMaior]:
               posicaoMaior = localizacao

       temp = lista[preencher]
       lista[preencher] = lista[posicaoMaior]
       lista[posicaoMaior] = temp

lista = random.sample(range(1, 50), 5)
selection_sort(lista)
print(lista)

import random
def insertion_sort(lista):
   for index in range(1,len(lista)):

     currentvalue = lista[index]
     position = index

     while position>0 and lista[position-1]>currentvalue:
         lista[position]=lista[position-1]
         position = position-1

     lista[position]=currentvalue

lista = random.sample(range(1, 50), 8)
insertion_sort(lista)
print(lista)