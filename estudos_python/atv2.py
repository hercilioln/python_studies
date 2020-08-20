from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (0, 10):
    for j in range(0, 3):
        matriz[i][j] = randint(1, 100)

for i in range(0, 10):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
