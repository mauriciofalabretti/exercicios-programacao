import re

#Função para validar o nome
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            name = str(input(mensagem)).strip()
            if re.search(r'\d', name) or len(name) == 0:
                raise ValueError('Nome inválido!')
            return name
        except ValueError:
            print(f'\033[0;91mNome não pode ser vazio ou conter números!\033[m Tente novamente!')

#Função para validar a entrada de inteiros(partidas e gols)
def valida_int(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                raise ValueError('Valor inválido!')
            return valor
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mValor não pode ser negativo!\033[m Tente novamente!')
            else:
                print(f'\033[0;91mValor deve ser um número inteiro válido!\033[m Tente novamente! {e}')

#Função para validar a resposta do usuário
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).strip().upper()[0]
            if resposta != 'S' and resposta != 'N': #Regra de negócio
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError:
            print(f'\033[0;91mDigite S para Sim ou N para Não!\033[m')


#Entrada de dados
lista_jogadores = list()
lista_gols = list()
while True:
    print('-' * 50)
    nome = valida_nome('Nome do Jogador: ')
    partidas = valida_int(f'Quantas partidas {nome} jogou? ')
    for i in range(partidas): #Loop para preencher a lista de gols
        gols = valida_int(f'Quantos gols na partida {i + 1}? ')
        lista_gols.append(gols)

    jogadores = { #Atribui as variáveis às chaves do dicionário
        'nome': nome,
        'partidas': partidas,
        'gols': lista_gols[:],
        'total': sum(lista_gols)
    }
    lista_gols.clear()
    lista_jogadores.append(jogadores.copy()) #Guarda o dicionário atual na lista
    continuar = valida_resposta('Deseja continuar? [S/N] ')
    if continuar == 'N':
        print('Saindo...')
        break

#Saída de dados, apresentação de resultados
print('=' * 50)
print('cod  nome            gols            total')
for i, jogador in enumerate(lista_jogadores): #Acessa o índice de cada jogador na lista de jogadores
    print(f"{i}   {jogador['nome']:15} {str(jogador['gols']):17} {jogador['total']:5}")
print('=' * 50)

dados_jogador = None
indices = list(range(len(lista_jogadores)))
while True:
    while True:
        dados_jogador = valida_int('Mostrar dados de qual jogador? (999 encerra) ')
        if dados_jogador == 999:
            break
        elif dados_jogador in indices:
            break
        else:
            print(f'O código {dados_jogador} não existe! Tente novamente!')
    if dados_jogador == 999:
        print('Saindo...')
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {lista_jogadores[dados_jogador]['nome']}')
    for i in range(lista_jogadores[dados_jogador]['partidas']): #Percorre o número de partidas do jogador
        print(f'   No jogo {i + 1} fez {lista_jogadores[dados_jogador]['gols'][i]} gols.') #Acessa o jogador dentro da lista e sua lista de gols, um por um
    print('-' * 50)
