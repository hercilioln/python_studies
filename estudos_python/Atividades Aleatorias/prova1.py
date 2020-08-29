homem50 = 0
mulher50 = 0
for c in range (0,5):
    nome = input('Qual seu nome?: ')
    sexo = input('Sexo Masculino=[M] ou Feminino=[F]: ').upper().strip()
    idade = int(input('Qual a sua idade?: '))
    if sexo in 'M' and idade > 50:
        homem50 += 1
    if sexo in 'F' and idade > 50:
        mulher50 += 1

if homem50 <= 1:
    print(f'A RodStuart possui {homem50} funcionário do sexo masculino com mais de 50 anos.')
elif homem50 >= 2:
    print(f'A RodStuart possui {homem50} funcionários do sexo masculino com mais de 50 anos.')
if mulher50 <=1:
    print(f'A RodStuart possui {mulher50} funcionário do sexo feminino com mais de 50 anos.')
elif mulher50 >= 2:
    print(f'A RodStuart possui {mulher50} funcionários do sexo feminino com mais de 50 anos.')