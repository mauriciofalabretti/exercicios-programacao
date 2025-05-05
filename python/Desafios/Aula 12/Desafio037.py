#Função para tratar exceções
def valida_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError as e:
            print(f'\033[0;91mErro! Valor inserido é diferente de inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados
num = valida_inteiro('Digite um valor inteiro: ')

#Usuário escolhe o tipo de conversão
liberado = False
while liberado == False:
    conversao = valida_inteiro('Qual será a base de conversão? \n'
                               '(1) para binário \n'
                               '(2) para octal \n'
                               '(3) para hexadecimal\n')
    if conversao != 1 and conversao != 2 and conversao != 3: #Garante que a opção seja válida
        print('Opção inválida! Tente novamente!')
    else:
        liberado = True

#Conversão ocorre de acordo com a opção escolhida
match conversao:
    case 1:
        print(f'O número \033[0;93m{num}\033[m em binário é: \033[0;96m{bin(num)}\033[m')
    case 2:
        print(f'O número \033[0;93m{num}\033[m em octal é: \033[0;96m{oct(num)}\033[m')
    case 3:
        print(f'O número \033[0;93m{num}\033[m em hexadecimal é: \033[0;96m{hex(num)}\033[m')