""" # foi passado como argumento 0.5 segundos na função sleep da biblioteca time
# para simular 1 minuto. Para o debug não ficar muito lento será usado dessa maneira
# interaja com o terminal para receber informações e simular ações em um sistema de atendimento

import matplotlib.pyplot as plt
import random
import time

attendants = [
    "Edem",
    "Alexo",
    "Ana Maria",
    "Fernanda"
]

rows = {
    'Primeira Fila': [1, 1],
    'Segunda Fila': [2, 1],
    'Terceira Fila': [3, 1],
    'Quarta Fila': [4, 1],
}

menu = " 1 - Visualizar Atendentes\n 2 - Atender Cliente\n 3 - Média de tempo nas filas por cliente\n 4 - Encerrar\n"
serviceMenu = " 1 - Receber dinheiro\n 2 - Troca de produto\n 3 - Devolução\n 4 - Encerrar Atendimento"
rowsMenu = " 1 - Primeira Fila\n 2 - Segunda Fila\n 3 - Terceira Fila\n 4 - Quarta Fila"
messageError = "[ERROR] Escolha uma opção válida"


def add_customer_to_queue(amountClient):
    terms = ''

    if rows['Primeira Fila'][0] > 11 or rows['Segunda Fila'][0] > 11 or rows['Terceira Fila'][0] > 11 or \
            rows['Quarta Fila'][0] > 11:
        return False

    if (rows['Primeira Fila'][0] < rows['Segunda Fila'][0] and rows['Primeira Fila'][0] < rows['Terceira Fila'][0] and \
            rows['Primeira Fila'][0] < rows['Quarta Fila'][0]):
        rows['Primeira Fila'][0] = amountClient
        terms = 'Primeira Fila'

    elif (rows['Segunda Fila'][0] < rows['Primeira Fila'][0] and rows['Segunda Fila'][0] < rows['Terceira Fila'][0] and \
          rows['Segunda Fila'][0] < rows['Quarta Fila'][0]):
        rows['Segunda Fila'][0] = amountClient
        terms = 'Segunda Fila'

    elif (rows['Terceira Fila'][0] < rows['Primeira Fila'][0] and rows['Terceira Fila'][0] < rows['Segunda Fila'][0] and \
          rows['Terceira Fila'][0] < rows['Quarta Fila'][0]):
        rows['Terceira Fila'][0] = amountClient
        terms = 'Terceira Fila'

    else:
        rows['Quarta Fila'][0] = amountClient
        terms = 'Quarta Fila'

    return terms


print("Organizando as filas...")
time.sleep(0.5)

while True:
    print("========== Atendimento Rápido ==========")
    print(menu)
    optionSelected = int(input("Digite a opção desejada: "))

    if optionSelected <= 0 or optionSelected > 4:
        print(messageError)
        continue

    if optionSelected == 5:
        print(rows)

    if optionSelected == 4:
        print("Desligando...")
        break

    if optionSelected == 1:
        print("Atendentes:")
        for attendant in attendants:
            print(attendant)

    if optionSelected == 2:
        counter = 0
        increment = 0

        while increment < 10:
            print(rowsMenu)
            rowsSelected = int(input("Escolha a fila para atender: "))
            rowSelected = ""

            if rowsSelected == 1:
                rowSelected = 'Primeira Fila'

            if rowsSelected == 2:
                rowSelected = 'Segunda Fila'

            if rowsSelected == 3:
                rowSelected = 'Terceira Fila'

            if rowsSelected == 4:
                rowSelected = 'Quarta Fila'

            if rowsSelected <= 0 or rowsSelected > 4:
                print(messageError)
                continue

            while counter < 10:
                print(serviceMenu)
                serviceSelected = int(input("Digite a opção desejada: "))

                if serviceSelected == 1:
                    amount = float(input("Digite a quantia recebida R$: "))
                    continue

                if serviceSelected == 2:
                    print("Produto trocado com sucesso")
                    continue

                if serviceSelected == 3:
                    luck = random.randint(0, 1)

                    if luck == 0:
                        print("Devolução NÃO ACEITA. Por favor verifique os termos.")
                    else:
                        print("Devolução aceita com sucesso.")
                    continue

                if serviceSelected == 4:
                    rows[rowSelected][1] = random.randint(5, 15)
                    rows[rowSelected][0] = rows[rowSelected][0] - 1
                    add_customer_to_queue(random.randint(3, 11))
                    print("TEMPO DO CLIENTE NA FILA:", rows[rowSelected][1], "MINUTOS")
                    counter = 10
                    increment = 10

                counter = counter + 1

                increment = increment + 1

    if optionSelected == 3:
        rowTime = [rows['Primeira Fila'][1], rows['Segunda Fila'][1], rows['Terceira Fila'][1], rows['Quarta Fila'][1]]
        namesRows = ["Primeira Fila", "Segunda Fila", "Terceira Fila", "Quarta Fila"]
        plt.title('Tempo médio dos clientes por fila em minutos')
        plt.xlabel('Filas')
        plt.ylabel('Tempo em minutos')
        plt.bar(namesRows, rowTime, color='green')
        plt.show() """





import os
import zlib
from contextlib import contextmanager

COMPRESSION = 9
MSG_END_TOKEN = b'EOM'
NUL_BYTE = b'\x00'
READ_CHUNK = 2048
INDEX_CHUNK = 50
MSG_END_TOKEN_SIZE = 3


class Queue:
    def __init__(self, filename):
        try:
            self.q = open(filename, 'r+b')
        except FileNotFoundError:
            self.q = open(filename, 'w+b')

    def __del__(self):
        self._commit()
        self.q.close()

    def enqueue(self, message):
        self.q.seek(0)
        idx = self.q.read(INDEX_CHUNK + MSG_END_TOKEN_SIZE)
        # emtpy file, writing dummy index
        with self._commit():
            if not idx:
                self.q.write(NUL_BYTE * INDEX_CHUNK)
                self.q.write(MSG_END_TOKEN)
                pos = self.q.tell()
                self.q.seek(0)
                self.q.write(bytes(str(pos), encoding='utf-8'))
            self.q.seek(0, 2)
            self.q.write(zlib.compress(bytes(message, encoding='utf-8'), COMPRESSION))
            self.q.write(MSG_END_TOKEN)

    def dequeue(self):
        self.q.seek(0)
        first_msg = None
        second_msg = None
        data = b''
        first_msg_stops_at = -1
        second_msg_stops_at = -1
        idx = self.q.read(INDEX_CHUNK + MSG_END_TOKEN_SIZE)
        if idx:
            idx = int(idx.rstrip(NUL_BYTE + MSG_END_TOKEN))
            self.q.seek(idx)
        else:
            return None

        while True:
            chunk = self.q.read(READ_CHUNK)
            if chunk == b'' or second_msg_stops_at != -1:
                break
            data += chunk
            first_msg_stops_at = data.find(MSG_END_TOKEN)
            if first_msg_stops_at != -1:
                second_msg_stops_at = data.find(MSG_END_TOKEN, first_msg_stops_at + MSG_END_TOKEN_SIZE)

        if data:
            if first_msg_stops_at != -1:
                with self._commit():
                    first_msg = data[0:first_msg_stops_at]
                    if second_msg_stops_at != -1:
                        #updates index pointing to next message
                        self.q.seek(0)
                        self.q.write(bytes(str(idx + len(first_msg) + MSG_END_TOKEN_SIZE), encoding='utf-8'))
                    else:
                        # all msgs consumed
                        self.q.seek(0)
                        self.q.truncate()

                return zlib.decompress(first_msg).decode('utf-8')
        return None

    @contextmanager
    def _commit(self):
        yield
        self.q.flush()
        os.fsync(self.q.fileno())