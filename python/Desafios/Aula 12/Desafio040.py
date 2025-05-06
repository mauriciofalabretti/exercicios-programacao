#Função para tratamento de exceções
def valida_notas(mensagem):
    while True:
        try:
            n = float(input(mensagem))
            if n < 0:
                raise ValueError('Nota menor que zero')
            return n
        except ValueError as e:
            if 'Nota menor que zero' in str(e):
                print(f'\033[0;91mValor não pode ser menor que zero!\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada das notas pelo usuário
n1 = valida_notas('Digite a primeira nota: ')
n2 = valida_notas('Digite a segunda nota: ')

#Cálculo da média e verificação da situação acadêmica
media = (n1 + n2) / 2
print(f'A média do(a) aluno(a) é: \033[0;94m{media:.1f}\033[m')

if media < 5:
    print(f'Situação: \033[0;91mReprovado!\033[m')
elif media >= 5 and media < 7:
    print(f'Situação: \033[0;93mEm Recuperação!\033[m')
else:
    print(f'Situação: \033[0;92mAprovado!\033[m')