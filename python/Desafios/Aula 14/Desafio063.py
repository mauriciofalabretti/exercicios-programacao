#Função para validar entrada de inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            num = int(input(mensagem))
            if num <= 0:
                raise ValueError('Valor inválido!')
            return num
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mDigite um número maior que zero!\033[m {e}')
            else:
                print(f'\033[0;91mDado deve ser do tipo inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Entrada de dados
n = valida_inteiros('Informe o tamanho da Sequência de Fibonacci desejada: ')

#Lógica principal
a = 0
b = 1
c = a + b

i = 1
while i <= n:
    if i == 1 and n == 1:
        print(f'\033[0;95m{a}\033[m', end=' ')
    elif i == 1 and n > 1:
        print(f'\033[0;95m{a}\033[m ->', end=' ')
    elif i == 2:
        print(f'\033[0;95m{b}\033[m', end=' ')
    else:
        print(f'-> \033[0;95m{c}\033[m', end=' ')
        a = b
        b = c
        c = a + b
    i += 1
