matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
soma = media = 0
for i in range (0, 5):
    for j in range(0, 5):
        matriz[i][j] = int(input(f'Digite um valor para a posição {i+1,j+1}: '))

for i in range(0, 5):
    for j in range(0, 5):
        print(f'[{matriz[i][j]:^5}]', end='')
        soma += matriz[i][j]
    print()

media = soma / len(matriz)
print(f'A soma dos valores digitados é igual a {soma}.')
print(f'A média dos valores digitados é igual a {media}.')
