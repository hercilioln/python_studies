""" matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
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

 """

"""  #listas

a = [2,1,3,4,5,8,2,3]
b = [9,2,4,6,8,1,2,0]
c = [0] * 8
soma  = 0

for i in range(0, len(a),1):
	c[i] = a[i] + b[i]
	print('Soma de  {} + {} = {}' . format(a[i],b[i],c[i]))
	soma = soma + c[i]

print('Soma total de A + B : ',soma) """

