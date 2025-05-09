from math import pow

#Função para validar o peso e altura
def valida_medida(mensagem):
    while True:
        try:
            m = float(input(mensagem))
            if m <= 0:
                raise ValueError('Medida Inválida!')
            return m
        except ValueError as e:
            if 'Medida Inválida!' in str(e):
                print(f'\033[0;91mMedida não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados, usuário informa o peso e altura
peso = valida_medida('Informe o seu peso: ')
altura = valida_medida('Informe a sua altura: ')

#Calcula e mostra o IMC
imc = peso / (pow(altura, 2))
print(f'IMC: \033[0;33m{imc:.1f}\033[m', end='')

#Verifica o enquadramento do IMC
if imc < 18.5:
    print(f' | Status: \033[0;34mAbaixo do Peso\033[m')
elif imc < 25:
    print(f' | Status: \033[0;34mPeso Ideal\033[m')
elif imc < 30:
    print(f' | Status: \033[0;34mSobrepeso\033[m')
elif imc < 40:
    print(f' | Status: \033[0;34mObesidade\033[m')
else:
    print(f' | Status: \033[0;34mObesidade Mórbida\033[m')
