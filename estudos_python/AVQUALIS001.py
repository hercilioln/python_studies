""" Na loja existem 4 atendentes, e a
cada minuto chegam entre 3 e 11 clientes; cada atendente demora entre 5 e 15 minutos para atender um cliente.
Para cada atendente existe uma fila; os clientes escolhem aquela que está vazia ou menos pessoas. Para cada cliente
que entra na fila, deve-se registrar quanto tempo ficou na fila, (diferença entre o horário que chegou na fila e horário de
atendimento). O algoritmo ou programa deverá informar o tempo médio que cada cliente permaneceu na fila e o total de
atendimentos realizados por atendente. """


import numpy as np

lista1 = np.arange(0, 100, 6)
lista2 = np.random.randint(5,15,9)
lista3 = np.random.rand(2,3,4)

print(lista2)


"""  import matplotlib.pyplot as plt

nome_filas = ['Fila 1', 'Fila 2', 'Fila 3', 'Fila 4']
media_filas = [10, 6, 8,6]

plt.xlabel('Filas')
plt.ylabel('Média de Tempo na Fila')
plt.plot(nome_filas, media_filas)
plt.show() """
