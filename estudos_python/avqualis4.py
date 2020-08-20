import time
import timeit

class Pessoa:
    def init(self,entrada,atendimento):
        self.entrada=entrada
        self.atendimento=atendimento
        self.saida_horario =""

    def entrando(self,ultimo_saida):
        self.saida_horario =ultimo+ atendimento

class Caixa:
    def init(self):
        self.fila=[]
        atendidos=0

    def add(self,pessoa):
        self.fila.append(pessoa)
        atendidos= antendidos +1

    def check(self,tempo):
        var = 0;
        for i in self.fila:
            if i.saida_horario >= tempo: #tempo é meramente ilustrativo, necessario de s.split para realizar
                var = var+1
        return var

    def tempo_ultimo():
        var = self.fila.index(atendidos-1)
        return var.self.saida_horario

i = 0 
caixa = Caixa()  #pode dar erro aqui, necessario checar como chamar as classes corretamente
caixa2 = Caixa()
caixa3 = Caixa()
while(i!=1):
    i=input("deseja iserir mais algum clinete se sim apete qualququer coisa menos 1")
    if(i!=1):
        hora,atendimente=("coloque a hora de chegada e o tempo de atendimento")
        pessa = Pessoa(hora,atendimento)
        if(caixa.check(pessoa.entrada)<=caixa2.check(pessoa.entrada)<=caixa3.check(pessoa.entrada)):
            pessoa.entrando(caixa.tempo_ultimo())
            caixa.add(pessoa)
        elif(caixa2.check(pessoa.entrada)<=caixa1.check(pessoa.entrada)):
            pessoa.entrando(caixa2.tempo_ultimo())
            caixa2.add(pessoa)
        elif(caixa3.check(pessoa.entrada)<=caixa2.check(pessoa.entrada)):
             pessoa.entrando(caixa3.tempo_ultimo())
             caixa3.add(pessoa)

print("tudo") # "tudo" é meramente ilustrativo


#falta ajustar o tempo com s.split(",")
#falta completar o while com caixa 4
#falta printar o resultado
#falta testar o codigo