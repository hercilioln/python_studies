equipe1 = []
equipe2 = []
equipe3 = []
equipe4 = []

alunos = []

while True:
    if len (alunos)>28:
        print("Todas as equipes já estão formadas.")
        break;
    novoAluno = input("Digite seu nome para se juntar a uma equipe: ")
    alunos.append(novoAluno)
for aluno in alunos:
    if len (equipe1)<7:
        equipe1.append(aluno)
    elif len (equipe2)<7:
        equipe2.append(aluno)
    elif len (equipe3)<7:
        equipe3.append(aluno)
    elif len (equipe4)<7:
        equipe4.append(aluno)

print(equipe1)
print(equipe2)
print(equipe3)
print(equipe4)