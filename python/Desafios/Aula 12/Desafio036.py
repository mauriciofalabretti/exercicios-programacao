#Montando a interface
print('=' * 30)
print('     EMPRÉSTIMO BANCÁRIO')
print('=' * 30)

#Função com tratamento de erros e validação
def valida_valores(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0: #Regra de Negócio
                raise ValueError('Valor Inválido')
            return valor
        except ValueError as e:
            if 'Valor Inválido' in str(e):
                print(f'\033[1;91mO valor não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[1;91mO tipo de valor inserido é inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[1;91mErro inesperado!\033[m {e}')


#Entrada de dados
valor_casa = valida_valores('Valor do imóvel: R$ ')
salario = valida_valores('Digite o salário: R$ ')
quantos_anos = 0

##Validação da entrada de anos com tratamento de erros
liberado = False
while liberado == False:
    try:
        quantos_anos = int(input('Em quantos anos será pago: '))
        if quantos_anos <= 0:
            raise ValueError('Tempo Inválido')
        liberado = True
    except ValueError as e:
        if 'Tempo Inválido' in str(e):
            print(f'\033[1;91mQuantidade de anos não pode ser inferior ou igual a zero!\033[m {e}')
        else:
            print(f'\033[1;91mValor inserido do tipo inválido!\033[m {e}')
    except Exception as e:
        print(f'\033[1;91mErro inesperado! {e}')

#Cálculo das prestações
valor_prestacao = valor_casa / (quantos_anos * 12)

#Cálculo de 30% do salário
perc_salario = salario * 0.30

#Cálculo do empréstimo possível
emprestimo_possivel = perc_salario * 12 * quantos_anos

#Condição para verificar a liberação do empréstimo
if valor_prestacao > perc_salario:
    print(f'\nO valor da prestação de \033[0;93mR$ {valor_prestacao:.2f}\033[m ultrapassa os'
          f' \033[0;95mR$ {perc_salario:.2f}\033[m correspondentes ao percentual permitido'
          f' para o empréstimo.\n'
          f'\033[0;91mEmpréstimo recusado!\033[m')
    print(f'Com as condições apresentadas pelo(a) cliente, ele pode optar'
          f' por um empréstimo de R$ {emprestimo_possivel:.2f}')
else:
    print(f'\n\033[1;92mEmpréstimo concedido no valor de {valor_casa:.2f}!\033[m\n'
          f'Valor das parcelas: \033[0;94m{valor_prestacao:.2f}')
