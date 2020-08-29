""" Na loja existem 4 atendentes, e a
cada minuto chegam entre 3 e 11 clientes; cada atendente demora 
entre 5 e 15 minutos para atender um cliente.
Para cada atendente existe uma fila; os clientes escolhem aquela 
que está vazia ou menos pessoas. Para cada cliente
que entra na fila, deve-se registrar quanto tempo ficou na fila, 
(diferença entre o horário que chegou na fila e horário de
atendimento). O algoritmo ou programa deverá informar o tempo médio 
que cada cliente permaneceu na fila e o total de
atendimentos realizados por atendente. """

import matplotlib.pyplot as plt
import random
import time
import numpy as np


filas = {'Fila 1': 'Atendende 1', 'Fila 2': 'Atendende 2', 'Fila 3': 'Atendende 3', 'Fila 4': 'Atendende 4',}

menu = "1 - Selecionar uma Fila\n2 - Tempo médio de fila\n3 - Relatório de atendimento" 
submenu = "1 - Encerrar atendimento"
menufilas = "1- FILA 1\n2- FILA 2\n3- FILA 3\n4- FILA 4"

lista3 = np.random.rand(2)

print("Organizando as filas...")
time.sleep(0.5)

while True:
    print("===== FILA DE ATENDIMENTO =====")
    print(menu)
    selecionar = int(input("Digite a opção desejada: "))

    if selecionar <=0 or selecionar > 6:
        print ("Digite uma opção válida!")
        continue

    if selecionar == 1:
        print (menufilas)
        selfila = int(input("Selecione uma fila para ser atendido: "))

        if selfila == 1:
            selfila = 'Fila 1'
        if selfila == 2:
            selfila = 'Fila 2'
        if selfila == 3:
            selfila = 'Fila 3'
        if selfila == 4:
            selfila = 'Fila 4'
        
        print(submenu)
        subsel = int(input("Encerre o atendimento: "))

        if subsel == 1:
            print(submenu)
            filas[selfila][1] = random.randint(5, 15)
            filas[selfila][0] = filas[selfila][0] - 1
            print("Tempo do cliente na fila: ", filas[selfila][1])
            counter = 10
            increment = 10
        counter = counter + 1
        increment = increment + 1



""" plt.xlabel('Filas')
plt.ylabel('Média de Tempo na Fila')
plt.bar(filas, selfilas)
plt.show()
 """


        

