from random import randint
from time import sleep

jogadores = {'Jogador1': None, 'Jogador2': None, 'Jogador3': None, 'Jogador4': None}

print('Valor sorteados:')
for k, v in jogadores.items():
    jogadores[k] = randint(1, 6)
    print(f'   O {k} tirou {jogadores[k]}') #Acessa o valor da chave
    sleep(1)

jog_ordenados = dict(sorted(jogadores.items(), reverse=True, key=lambda item: item[1]))


print('Ranking dos jogadores:')
print('-' * 40)
cont = 1
for k, v in jog_ordenados.items():
    print(f'   {cont}º lugar: {k} com {v}')
    sleep(1)
    cont += 1
