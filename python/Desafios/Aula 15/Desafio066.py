#Função para validar a entrada de inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mValor informado deve ser um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Lógica principal com entrada e processamento de dados
soma = 0
cont = 0
while True:
    num = valida_inteiros('Digite um número (999 para parar): ')
    if num == 999:
        break
    soma += num
    cont += 1

#Apresentação de resultados
print(f'\nA soma dos valores digitados é \033[0;34m{soma}\033[m')
print(f'Foram digitados \033[0;34m{cont}\033[m números')
