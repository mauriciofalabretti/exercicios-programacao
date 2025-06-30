import re
import sys

#Função para validar nome
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            name = str(input(mensagem)).strip()
            if re.search(r'\d', name) or len(name) == 0:
                raise ValueError('Nome inválido!')
            return name
        except ValueError as e:
            print(f'\033[0;91mNome não pode conter números ou ser vazio!\033[m Tente novamente! {e}')

#Função para validar entrada de inteiros
def valida_int(mensagem: str) -> int:
    while True:
        try:
            num = int(input(mensagem))
            if num < 0: #Regra de negócio
                raise ValueError('Valor inválido!')
            return num
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mValor não pode ser negativo!\033[m Tente novamente!')
            else:
                print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente!')


#Entrada de dados
nome = valida_nome('Nome do jogador: ')
partidas = valida_int(f'Quantas partidas {nome} jogou? ')
if partidas == 0: #Se o jogador não jogou nenhuma partida, o programa não precisa continuar
    sys.exit(f'{nome} não jogou nenhuma partida.')

##Loop para preenchimento da lista
lista_gols = list()
for i in range(partidas):
    lista_gols.append(valida_int(f'Quantos gols na partida {i + 1}? '))

##Estruturação e preenchimento do dicionário
dic_jogador = {
    'nome': nome,
    'gols': lista_gols,
    'total': sum(lista_gols)
}

#Apresentação de valores
print('-' * 50)
print(dic_jogador)
print(f'O campo nome tem o valor {dic_jogador['nome']}.')
print(f'O campo gols tem o valor {dic_jogador['gols']}.')
print(f'O campo total tem o valor {dic_jogador['total']}.')
print('-' * 50)

print(f'O jogador {dic_jogador['nome']} jogou {partidas} partidas.')
for i, v in enumerate(lista_gols): #Acessa o índice e o número de gols da lista_gols
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dic_jogador['total']} gols.')
