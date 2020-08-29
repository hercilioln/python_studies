""" vetor = []
maior = menor = 0
for c in range(0, 10):
    vetor.append(int(input(f'Digite um valor: ')))
for c in vetor:
    if c == 0:
        c = maior
        c = menor
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'O maior número digitado for {maior} e o menor número digitado foi {menor}.')
 """

""" vetor = []
maior = 0
menor = 0

for c in range (0, 10):
    vetor.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = vetor[c]
    else:
        if vetor[c] > maior:
            maioror = vetor[c]
        if vetor[c] < menor:
            menor = vetor[c]

#print('=-' * 30)
print(f'Você digitou os valores {vetor}')
print (f'O maior valor digitado foi {maior}')
print (f'O menor valor digitado foi {menor}') """

""" vetor = []
maior = []
menor = []
for c in range(0, 10):
    val = int(input(f'Digite um valor na posição {c}: '))
    vetor.append(val)
for valores in enumerate(vetor):
    if valores == max(vetor):
        maior.append(vetor)
    if valores == min(vetor):
        menor.append(vetor)
print(f'Você digitou os valores {vetor}')
print(f'O maior valor digitado foi: {max(vetor)}')
print(f'O menor valor digitado foi: {min(vetor)}') """


""" notas = []
soma = 0
num = 0
for c in range(0, 15):
    num = notas.append(float(input(f'Nota da prova do aluno {c}: ')))
    soma += num
    num = 0
media = soma / len(notas)
print(f'A média da turma foi {media}.') """


notas = []
soma = 0
for nota in range(0, 15):
    notas.append(float(input(f'Digite a nota da prova do aluno {nota}: ')))
    soma += nota
media = (soma / len(notas))

print('=-' * 30)
print(f'As notas foram: {notas}')
print(f'A média geral é: {media}')
