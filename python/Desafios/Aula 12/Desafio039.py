from datetime import date

#Função para tratamento de erros referente ao ano
def valida_ano(mensagem):
    while True:
        try:
            ano = int(input(mensagem))
            if ano <= 0:
                raise ValueError('MenorIgualZero')
            return ano
        except ValueError as e:
            if 'MenorIgualZero' in str(e):
                print(f'\033[0;91mAno não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mAno deve ser do tipo inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Função para tratamento de erros sobre a entrada do sexo
def valida_string(mensagem: str) -> str:
    while True:
        try:
            s = str(input(mensagem)).upper().strip()
            if s not in {'M', 'F'}:
                raise ValueError('Selecione M ou F')
            return s
        except ValueError as e:
            if 'Selecione M ou F' in str(e):
                print(f'\033[0;91mOpção inválida!\033[m {e}')
            else:
                print(f'\033[0;91mTipo inserido é inválido! {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[0;91m {e}')


#Entrada de dados
sexo = valida_string('Informe o seu sexo: [M/F] ')

if sexo == 'F':
    print(f'O alistamento militar não é obrigatório para pessoas do sexo feminino!')
else:
    ano_nascimento = valida_ano('Informe o seu ano de nascimento: ')
    #Cálculo da idade
    ano_atual = date.today()
    idade = ano_atual.year - ano_nascimento

    #Verifica as condições de alistamento
    if idade == 18:
        print(f'Você já possui \033[0;93m{idade} anos\033[m. \033[0;95mEstá na hora de se alistar!\033[m')
    elif idade < 18:
        print(f'Você possui \033[0;93m{idade} anos\033[m. Faltam \033[0;95m{18 - idade} anos\033[m para seu alistamento.')
        print(f'Deverá realizar o alistamento em \033[0;95m{ano_atual.year + (18 - idade)}\033[m.')
    else:
        print(f'Você possui \033[0;93m{idade} anos\033[m. Seu período de alistamento ocorreu há \033[0;95m{idade - 18} anos\033[m.')
        print(f'Deveria ter se alistado em \033[0;95m{ano_atual.year - (idade - 18)}\033[m.')