#Função para tratamento de exceções
def valida_inteiros(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError as e:
            print(f'\033[0;91mO valor inserido é do tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados
num1 = valida_inteiros('Digite um valor inteiro: ')
num2 = valida_inteiros('Digite outro valor inteiro: ')

#Comparando os valores
if num1 > num2:
    print(f'\033[0;94m{num1}\033[m é maior que {num2}')
elif num1 < num2:
    print(f'\033[0;94m{num2}\033[m é maior que {num1}')
else:
    print(f'\033[0;95mOs números são iguais!\033[m')