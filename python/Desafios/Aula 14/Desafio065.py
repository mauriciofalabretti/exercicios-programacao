#Função para validar inteiros
def valida_inteiros(mensagem: str) -> int:
    '''Valida entradas inteiras até receber um número válido'''
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mValor deve ser do tipo inteiro!\033[m {e}')
        except KeyboardInterrupt:
            print(f'\033[0;93mOperação cancelada pelo usuário!\033[m')


#Função para validar strings
def valida_string(mensagem: str) -> str:
    '''Valida a string até que ela atenda as regras de negócio e de tipo'''
    lista = {'S', 'N'}
    while True:
        try:
            s = str(input(mensagem)).strip().upper()[0]
            if s not in lista: #Regra de negócio
                raise ValueError('Opção inválida!')
            return s
        except ValueError as e:
                print(f'\033[0;91mDigite "S" ou "N"!\033[m {e}')
        except KeyboardInterrupt:
            print(f'\033[0;93mOperação cancelada pelo usuário!\033[m')


#Loop para entrada e processamento de dados
continuar = 'S'
cont = 0
soma = 0
while 'N' not in continuar:
    num = valida_inteiros('Digite um número inteiro: ')
    if cont == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    continuar = valida_string('Deseja continuar? [S/N] ')

#Apresentação dos resultados
print(f'\nO \033[0;95mmaior\033[m valor informado foi: \033[0;94m{maior}\033[m')
print(f'O \033[0;95mmenor\033[m valor informado foi: \033[0;94m{menor}\033[m')
print(f'Foram informados \033[0;95m{cont}\033[m números')
if cont > 0:
    media = soma / cont
    print(f'A \033[0;95mmédia\033[m dos números informados é: \033[0;94m{media:.2f}\033[m')
else:
    print(f'A \033[0;95mmédia\033[m para zeros é inexiste')
