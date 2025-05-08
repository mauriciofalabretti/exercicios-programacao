#Função para tratamento de erros de entrada
def valida_entrada(mensagem):
    while True:
        try:
            l = float(input(mensagem))
            if l <= 0:
                raise ValueError('Medida Inválida!')
            return l
        except ValueError as e:
            if 'Medida Inválida!' in str(e):
                print(f'\033[0;91mValor não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados
l1 = valida_entrada('Digite o primeiro lado: ')
l2 = valida_entrada('Digite o segundo lado: ')
l3 = valida_entrada('Digite o terceiro lado: ')

#Verifica se os lados formam um triângulo
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print(f'As medidas informadas \033[0;92mformam um triângulo!\033[m')

    # Verifica o tipo dos triângulos (Equilátero, Isósceles ou Escaleno)
    if l1 == l2 == l3:
        print(f'O triângulo é \033[0;34mEQUILÁTERO\033[m')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print(f'O triângulo é \033[0;34mESCALENO\033[m')
    else:
        print(f'O triângulo é \033[0;34mISÓSCELES\033[m')
else:
    print(f'As medidas informadas \033[0;31mnão formam um triângulo!\033[m')

