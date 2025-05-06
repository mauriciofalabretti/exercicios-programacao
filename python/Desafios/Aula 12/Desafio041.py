from datetime import datetime

#Função para validar idade
def valida_ano():
    while True:
        try:
            a = int(input('Digite o ano de seu nascimento: '))
            if a <= 0:
                raise ValueError('Ano Inválido!')
            return a
        except ValueError as e:
            if 'Ano Inválido!' in str(e):
                print(f'\033[0;91mAno não pode ser menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mO tipo de dado inserido é inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[mErro inesperado!\033[m {e}')

#Entrada de dados com função validadora e cálculo de idade
ano_nasc = valida_ano()
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc

#Verifica e apresenta a categoria do atleta de natação
if idade <= 9:
    print(f'Você possui: \033[0;93m{idade} anos\033[m. | \033[0;96mCategoria: MIRIM\033[m')
elif idade <= 14:
    print(f'Você possui: \033[0;93m{idade} anos\033[m. | \033[0;96mCategoria: INFANTIL\033[m')
elif idade <= 19:
    print(f'Você possui: \033[0;93m{idade} anos\033[m. | \033[0;96mCategoria: JUNIOR\033[m')
elif idade <= 20:
    print(f'Você possui: \033[0;93m{idade} anos\033[m. | \033[0;96mCategoria: SÊNIOR\033[m')
else:
    print(f'Você possui: \033[0;93m{idade} anos\033[m. | \033[0;96mCategoria: MASTER\033[m')