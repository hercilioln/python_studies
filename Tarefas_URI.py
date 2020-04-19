'''#Problema 1095 - Sequencia IJ 1
I = 1
J = 60

while J >= 0:
    print('I={} J={}'.format(I, J))
    I = I + 3
    J = J - 5'''






'''
#problema 1096 - Sequencia IJ 2

I = 1
J = 7

while I <= 9:
    while J >= 5:
        print('I={} J={}'.format(I, J))
        J = J - 1
    I = I + 2
    J = 7
'''








'''
# URI 1113
while True:
    x, y = list(map(int, input().split()))

    if (x == y):
        break

    if (x > y):
        print("Decrescente")
    else:
        print("Crescente")

'''






'''
# URI 1042
N = int(input())
X = 1

for i in range(1, N + 1):
    print('{} {} {} PUM'.format(X, X+1, X+2))
    X = X + 4
'''








'''
# URI 1012

value = input().split(" ")

A, B, C = value

A = float(A)
B = float(B)
C = float(C)

TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * (C * C)
TRAPEZIO = ((A + B)/2) * C
QUADRADO = B * B
RETANGULO = A * B

print('TRIANGULO: %0.3f' % (TRIANGULO)) #concatenação é com % e não com virgula
print('CIRCULO: %0.3f' % (CIRCULO))
print('TRAPEZIO: %0.3f' % (TRAPEZIO))
print('QUADRADO: %0.3f' % (QUADRADO))
print('RETANGULO: %0.3f' % (RETANGULO))

'''




'''
#URI 1012
valor = input().split(" ")

A,B,C = valor
pi = 3.14159

TRIANGULO = (float(A) * float(C)) / 2
CIRCULO = pi * (float(C) * float(C))
TRAPEZIO = ((float(A) + float(B))/2) * float(C)
QUADRADO = float(B) * float(B)
RETANGULO = float(A) * float(B)

print(
    "TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" %(
        TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO
    )
)

'''








