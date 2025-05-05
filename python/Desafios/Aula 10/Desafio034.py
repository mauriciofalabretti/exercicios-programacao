#Entrada de dados via teclado com o tipo float e tratamento de erros
liberado = False
while liberado == False:
    try:
        salario = float(input('Digite o salário do(a) funcionário(a): R$ '))
        if salario <= 0:
            raise ValueError('Salário_Inválido')
        liberado = True
    except ValueError as e:
        if 'Salário_Inválido' in str(e):
            print(f'{'\033[1;91m'}ERRO! Salário deve ser maior que zero!{'\033[m'}')
        else:
            print(f'{'\033[1;91m'}ERRO! Digite um valor númerico válido!{'\033[m'}')
    except Exception as e:
        print(f'{'\033[1;91m'}Erro inesperado!{'\033[m'} {e}')

#Cálculo de aumento do salário
if salario > 1250.00:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

#Apresentação do salário pós-aumento
print(f'O salário após o aumento será de {'\033[4;92m'}R$ {novo_salario:.2f}{'\033[m'}')