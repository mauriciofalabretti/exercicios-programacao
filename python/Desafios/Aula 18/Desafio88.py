from random import sample
from time import sleep

#Função para validar entrada de inteiros
def valida_int(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente! {e}')


print('-' * 40)
print(f'{f'JOGA NA MEGA SENA':^40}')
print('-' * 40)

#Entrada de dados para saber quantos jogos serão feitos
sorteios = valida_int('Informe quantos jogos devem ser sorteados: ')

#Uso do list comprehension para definir a lista de jogos
jogos = [[] for _ in range(sorteios)]

#Loop de sorteio
print(f'-=' * 3, end='')
print(f'SORTEANDO {sorteios} JOGOS', end='')
print(f'-=' * 3)
for i in range(sorteios):
    jogos[i] = (sorted(sample(range(1, 61), 6))) #O sample() retorna uma lista

#Loop de apresentação de valores
for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)
print(f'-=' * 6, end='')
print('< BOA SORTE! >', end='')
print(f'-=' * 6)
