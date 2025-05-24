#Função para validar idades
def valida_idades(mensagem: str) -> int:
    while True:
        try:
            i = int(input(mensagem))
            if i <= 0: #Regra de negócio
                raise ValueError('Idade inválida!')
            return i
        except ValueError as e:
            if 'Idade inválida!' in str(e):
                print(f'\033[0;91mA idade deve ser maior que zero!\033[m {e}')
            else:
                print(f'\033[0;91mA idade deve ser um número válido!\033[m {e}')
        except KeyboardInterrupt as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para validar entradas do tipo string
def valida_string(mensagem: str) -> str:
    sexos = {'M', 'F', 'm', 'f'}
    continua = {'S', 'N', 's', 'n'}
    while True:
        try:
            s = str(input(mensagem)).strip()
            if s.isalpha() == False:
                raise ValueError('Tipo inválido!')
            if 'sexo' in mensagem:
                if s not in sexos:
                    raise ValueError('Sexo inválido!')
            elif 'continuar' in mensagem:
                if s not in continua:
                    raise ValueError('Opção inválida!')
            return s
        except ValueError as e:
            if 'Tipo inválido!' in str(e):
                print(f'\033[0;91mEsperava uma entrada do tipo caractere!\033[m {e}')
            elif 'Sexo inválido!' in str(e):
                print(f'\033[0;91mDigite M para masculino ou F para feminino!\033[m {e}')
            elif 'Opção inválida!' in str(e):
                print(f'\033[0;91mDigite S para continuar ou N para encerrar!\033[m {e}')
        except KeyboardInterrupt as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Lógica principal para o cadastro de pessoas
cont_maiores = 0
cont_masc = 0
cont_fem_menos_vinte = 0
while True:
    print(f'{f' CADASTRO ':=^30}')
    idade = valida_idades('Informe a idade: ')
    if idade > 18:
        cont_maiores += 1
    sexo = valida_string('Informe o sexo: [M/F] ').upper()
    if sexo == 'M':
        cont_masc += 1
    elif sexo == 'F' and idade < 20:
        cont_fem_menos_vinte += 1

    continuar = valida_string('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break

#Apresentação de resultados
print(f'\033[0;32m{cont_maiores}\033[m pessoas têm mais de 18 anos.')
print(f'Foram cadastrados \033[0;32m{cont_masc}\033[m homens.')
print(f'\033[0;32m{cont_fem_menos_vinte}\033[m mulheres têm menos de 20 anos.')
