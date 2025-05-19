#Função para validar a entrada de inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if n < 0:
                raise ValueError('Tente novamente!')
            return n
        except ValueError as e:
            if 'Tente novamente!' in str(e):
                print(f'\033[0;91mNúmero não pode ser inferior à zero!\033[m {e}')
            else:
                print(f'\033[0;91mEsperava um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para cálculo fatorial
def calcular_fatorial(num: int) -> int:
    fatorial = 1
    while num > 0:
        fatorial *= num
        num -= 1
    return fatorial


#Entrada de dados
num = valida_inteiros('Digite um número para ver o seu fatorial: ')

#Loop para cálculo do fatorial
'''fatorial = 1
print(f'\033[0;94m{num}!\033[m =', end=' ')
while num > 0:
    if num == 1:
        print(f'{num} =', end=' ')
    else:
        print(f'{num} x', end=' ')

    fatorial *= num
    num -= 1'''


#Apresentação de resultado
print(f'\033[0;94m{calcular_fatorial(num)}\033[m')

