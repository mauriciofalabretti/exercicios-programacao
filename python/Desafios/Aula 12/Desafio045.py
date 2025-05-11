from random import randint
from time import sleep

#Função para validar a entrada de dados e tratamento de exceções
def valida_entrada(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if n not in {1, 2, 3}:
                raise ValueError('Opção Inválida!')
            return n
        except ValueError as e:
            if 'Opção Inválida!' in str(e):
                print(f'\033[0;91mA opção escolhida deve ser 1, 2 ou 3.\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para construir a interface do jogo
def interface():
    print('=' * 30)
    print('|  Pedra, Papel ou Tesoura?  |')
    print('=' * 30)
    print(f'\033[0;94m(1) Pedra\n'
          f'(2) Papel\n'
          f'(3) Tesoura\033[m')

#Função para validar a condição de parada
def valida_string(mensagem: str) -> str:
    while True:
        try:
            s = str(input(mensagem)).strip().upper()
            if 'S' not in s and 'N' not in s:
                raise ValueError('Digite "S" para Sim e "N" para não!')
            return s
        except ValueError as e:
            if 'Digite "S" para Sim e "N" para não!' in str(e):
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Função para o placar final
def placar(vitorias, derrotas, empates: int):
    print('-' * 20)
    print(f'{' ESTATÍSTICAS: ':^22}\n'
          f'\033[0;96mJogador\033[m | \033[0;92m{vitorias} Vitória(s)\033[m\n'
          f'\033[0;91mOponente\033[m | \033[0;92m{derrotas} Vitória(s)\033[m\n'
          f'\033[0;95mEmpates\033[m | \033[0;92m{empates} Empate(s)\033[m')
    print('-' * 20)


#Constantes
pedra = 1
papel = 2
tesoura = 3

#Lógica principal do jogo
#Inicialização de variáveis de controle e contadoras
continua = 'S'
cont_vitorias = 0
cont_derrotas = 0
cont_empates = 0

while 'S' in continua:
    interface()
    jogador = valida_entrada('Pedra, Papel ou Tesoura? ')
    adversario = randint(1,3)
    print('Pedra...')
    sleep(0.7)
    print('Papel...')
    sleep(0.7)
    print('Tesoura!')
    sleep(0.7)
    if jogador == pedra:
        if adversario == papel:
            print('\033[0;93mPapel derrota Pedra!\033[m \033[0;95mVitória do oponente!\033[m')
            cont_derrotas = cont_derrotas + 1
        elif adversario == tesoura:
            print('\033[0;93mPedra derrota Tesoura!\033[m \033[0;95mVitória do jogador!\033[m')
            cont_vitorias = cont_vitorias + 1
        else:
            print('\033[0;93mPedra contra Pedra! O jogo empatou!\033[m')
            cont_empates = cont_empates + 1
    elif jogador == papel:
        if adversario == pedra:
            print('\033[0;93mPapel derrota Pedra!\033[m \033[0;95mVitória do jogador!\033[m')
            cont_vitorias = cont_vitorias + 1
        elif adversario == tesoura:
            print('\033[0;93mTesoura derrota Papel!\033[m \033[0;95mVitória do oponente!\033[m')
            cont_derrotas = cont_derrotas + 1
        else:
            print('\033[0;93mPapel contra Papel! O jogo empatou! \033[m')
            cont_empates = cont_empates + 1
    else:
        if adversario == pedra:
            print('\033[0;93mPedra derrota Tesoura!\033[m \033[0;95mVitória do oponente!\033[m')
            cont_derrotas = cont_derrotas + 1
        elif adversario == papel:
            print('\033[0;93mTesoura derrota Papel!\033[m \033[0;95mVitória do jogador!\033[m')
            cont_vitorias = cont_vitorias + 1
        else:
            print('\033[0;93mTesoura contra Tesoura! O jogo empatou!\033[m')
            cont_empates = cont_empates + 1
    continua = valida_string('Deseja continuar? [S/N] ')

#Apresentação do placar
placar(cont_vitorias, cont_derrotas, cont_empates)