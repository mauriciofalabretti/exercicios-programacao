#Função para validar entrada e tratar exceções
def valida_valor():
    while True:
        try:
            v = float(input('Digite o valor do produto: R$ '))
            if v <= 0:
                raise ValueError('Valor Inválido!')
            return v
        except ValueError as e:
            if 'Valor Inválido!' in str(e):
                print(f'\033[0;91mValor não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Função para validar e tratar exceções da opção escolhida pelo usuário
def valida_opcao(mensagem):
    while True:
        try:
            o = int(input(mensagem))
            if o != 1 and o != 2 and o != 3 and o != 4:
                raise ValueError('Opção Inválida!')
            return o
        except ValueError as e:
            if 'Opção Inválida!' in str(e):
                print(f'\033[0;91mOpção inexistente!\033[m {e}')
            else:
                print(f'\033[0;91mValor do tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados
valor_produto = valida_valor()

#Verifica opção de pagamento e calcula o valor do produto de acordo com ela
pagamento = valida_opcao('Informa a condição de pagamento:\n'
                         '(1) à vista dinheiro/cheque\n'
                         '(2) à vista no cartão\n'
                         '(3) até 2x no cartão\n'
                         '(4) 3x ou mais no cartão\n')

match pagamento:
    case 1:
        valor_final = valor_produto - (valor_produto * 0.10)
    case 2:
        valor_final = valor_produto - (valor_produto * 0.05)
    case 3:
        valor_final = valor_produto
    case 4:
        valor_final = valor_produto + (valor_produto * 0.20)

#Apresenta o valor a ser pago de acordo com a condição escolhida
print(f'O valor final do produto será de \033[0;36mR$ {valor_final:.2f}\033[m')

