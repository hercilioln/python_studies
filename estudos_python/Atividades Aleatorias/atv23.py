matriz1 = []
matriz2 = []
from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (0, 10):
    for j in range(0, 3):
        matriz[i][j] = randint(1, 100)
        if matriz [i][j] % 2 == 0:
            matriz1.append(matriz[i][j])
        else:
            matriz2.append(matriz[i][j])

for i in range(0, 10):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'Os elementos pares da matriz são {matriz1}')
print(f'Os elementos ímpares da matriz são {matriz2}')
