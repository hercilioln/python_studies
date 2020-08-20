func = {}
fun01 = []

for i in range(0,5):
    func.clear()
    func['nome'] = input(f'Nome do funcionário para avaliação: ')
    func['nota'] = int(input(f'Escolha uma nota de 0 a 10 para esse funcionario: '))
    fun01.append(func.copy())
ordenada = sorted(fun01, key=lambda k: k['nota'], reverse=True)
print(f'--RANKING DOS FUNCIONÁRIOS - RodGames-- \n {ordenada}')