from datetime import date

#Função para validar entrada
def valida_entrada(mensagem: str) -> int:
    while True:
        try:
            a = int(input(mensagem))
            if a <= 0: #Regras de Negócio
                raise ValueError('Valor Inválido!')
            return a
        except ValueError as e:
            if 'Valor Inválido!' in str(e):
                print(f'\033[0;91mNúmero não pode ser menor ou igual à zero!\033[m {e}')
            else:
                print(f'\033[0;91mDado inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Loop para entrada de dados e verificação de maioridade
ano_atual = date.today().year
cont_maiores = 0
cont_menores = 0

for i in range(7):
    ano_nasc = valida_entrada(f'Em que ano a {i + 1}º pessoa nasceu? ')
    if ano_atual - ano_nasc  >= 21:
        cont_maiores += 1
    else:
        cont_menores += 1

#Apresentação dos resultados
print(f'\033[0;92m{cont_maiores} pessoas são maiores de idade\033[m.')
print(f'\033[0;93m{cont_menores} pessoas são menores de idade\033[m.')
