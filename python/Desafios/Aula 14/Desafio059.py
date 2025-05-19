from math import pow, lcm
from time import sleep

#Função verifica as entradas de tipos inteiros e também trata das opções do usuário
def valida_inteiros(mensagem: str) -> int:
    alternativas = set(range(1, 12)) #Cria o conjunto de opções válidas
    while True:
        try:
            n = int(input(mensagem))
            if 'opção' in mensagem: #Se o input for relacionado às opções do menu
                if n not in alternativas: #Regra de negócio
                    raise ValueError('Opção inválida!')
            return n
        except ValueError as e:
            if 'Opção inválida!' in str(e):
                print(f'\033[0;91mVocê deve escolher um dos valores {alternativas}\033[m {e}')
            else:
                print(f'\033[0;91mDado deve ser um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para criar a interface do menu
def menu_interface():
    print(f'{' \033[0;34mMENU\033[m ':-^30}')
    print(f'\033[0;33m[ 1 ]\033[m \033[0;34msomar\033[m\n'
          f'\033[0;33m[ 2 ]\033[m \033[0;34msubtrair\033[m\n'
          f'\033[0;33m[ 3 ]\033[m \033[0;34mmultiplicar\033[m\n'
          f'\033[0;33m[ 4 ]\033[m \033[0;34mdividir\033[m\n'
          f'\033[0;33m[ 5 ]\033[m \033[0;34mresto\033[m\n'
          f'\033[0;33m[ 6 ]\033[m \033[0;34mmaior\033[m\n'
          f'\033[0;33m[ 7 ]\033[m \033[0;34mmenor\033[m\n'
          f'\033[0;33m[ 8 ]\033[m \033[0;34mpotenciação\033[m\n'
          f'\033[0;33m[ 9 ]\033[m \033[0;34mmmc\033[m\n'
          f'\033[0;33m[ 10 ]\033[m \033[0;34mnovos números\033[m\n'
          f'\033[0;33m[ 11 ]\033[m \033[0;34msair do programa\033[m')


#Entrada de dados
n1 = valida_inteiros('Digite o primeiro número: ')
n2 = valida_inteiros('Digite o segundo número: ')

#Processamento de dados, lógica principal
opcao = 0
while opcao != 11:
    menu_interface()
    opcao = valida_inteiros('Escolha a opção: ')
    match opcao: #Execução da opção escolhida
        case 1:
            print(f'\033[0;33mSoma:\033[m {n1} + {n2} = {n1 + n2}')
        case 2:
            print(f'\033[0;33mSubtração:\033[m {n1} - {n2} = {n1 - n2}')
        case 3:
            print(f'\033[0;33mMultiplicação:\033[m {n1} x {n2} = {n1 * n2}')
        case 4:
            print(f'\033[0;33mDivisão:\033[m {n1} / {n2} = {n1 / n2:.2f}')
        case 5:
            print(f'\033[0;33mResto:\033[m {n1} % {n2} = {n1 % n2}')
        case 6:
            print(f'\033[0;33mMaior:\033[m', end=' ')
            if n1 == n2:
                print('Os números são iguais!')
            else:
                print(max(n1, n2))
        case 7:
            print(f'\033[0;33mMenor:\033[m', end=' ')
            if n1 == n2:
                print('Os números são iguais!')
            else:
                print(min(n1, n2))
        case 8:
            print(f'\033[0;33mPotenciação:\033[m {pow(n1, n2):.2f}')
        case 9:
            print(f'\033[0;33mMMC:\033[m {lcm(n1, n2)}')
        case 10:
            print(f'\033[0;33mNovos Números:')
            n1 = valida_inteiros('Informe o novo valor: ')
            n2 = valida_inteiros('Informe o novo valor: ')
        case 11:
            print(f'\033[0;33mSaindo...\033[m')
    sleep(3)
