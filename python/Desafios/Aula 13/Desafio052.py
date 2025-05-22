#Função para validar inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if n <= 0: #Regra de negócio
                raise ValueError('Valor Inválido!')
            return n
        except ValueError as e:
            if 'Valor Inválido!' in str(e):
                print(f'\033[0;91mO valor não pode ser menor ou igual à zero!\033[m {e}')
            else:
                print(f'\033[0;91mO tipo de dado inserido é inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro Inesperado!\033[m {e}')

#Entrada de dados
numero = valida_inteiros('Informe um número: ')

#Verifica se o número informado é primo e mostra para o usuário
cont = 0
#Sendo divisível por qualquer número acima de 1 e abaixo do número informado, o contador recebe mais um
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1
        print(f'\033[0;93m{i}\033[m', end=' ')
    else:
        print(f'\033[0;94m{i}\033[m', end=' ')

#Se o contador tiver acumulado pelo menos 1, significa que o número não é primo
if cont != 2:
    print(f'\n\033[0;91mO número {numero} não é primo!\033[m\n'
          f'Ele foi divisível {cont} vezes!')
else:
    print(f'\n\033[0;92mO número {numero} é primo!\033[m\n'
          f'Ele é apenas divisível por 1 e a si próprio.')
