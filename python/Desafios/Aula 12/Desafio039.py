import datetime

#Função para tratamento de erros
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

#Entrada de dados
ano_nascimento = valida_ano('Informe o seu ano de nascimento: ')

#Cálculo da idade
ano_atual = datetime.datetime.now()
idade = ano_atual.year - ano_nascimento

#Verifica as condições de alistamento
if idade == 18:
    print(f'Você já possui \033[0;93m{idade} anos\033[m. \033[0;95mEstá na hora de se alistar!\033[m')
elif idade < 18:
    print(f'Você possui \033[0;93m{idade} anos\033[m. Faltam \033[0;95m{18 - idade} anos\033[m para seu alistamento.')
else:
    print(f'Você possui \033[0;93m{idade} anos\033[m. Seu período de alistamento ocorreu há \033[0;95m{idade - 18} anos\033[m.')