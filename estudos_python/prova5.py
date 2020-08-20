time1 = []
time2 = []
time3 = []
time4 = []

alunos = []

while True:
    if len (alunos)>28:
        print("Ops! Parece que todsas as equipes ja foram preenchidas! Aguarde sua vez. :( ")
        break;
    novoAluno = input("Você chegou agora! Ainda há vagas. Digite seu nome para juntar-se a uma equipe: ")
    alunos.append(novoAluno)
for aluno in alunos:
    if len (time1)<7:
        time1.append(aluno)
    elif len (time2)<7:
        time2.append(aluno)
    elif len (time3)<7:
        time3.append(aluno)
    elif len (time4)<7:
        time4.append(aluno)

print(time1)
print(time2)
print(time3)
print(time4)