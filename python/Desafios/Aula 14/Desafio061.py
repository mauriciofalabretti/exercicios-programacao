#Função para validar inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mDado inserido deve ser um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Entrada de dados
primeiro_termo = valida_inteiros('Informe o primeiro termo: ')
razao = valida_inteiros('Informe a razão: ')

#Loop para progressão aritmética
proximo_termo = primeiro_termo
i = 1
print(f'[\033[0;34m{primeiro_termo}\033[m]', end=' ')
while i <= 9:
    proximo_termo += razao
    print(f'[\033[0;34m{proximo_termo}\033[m]', end=' ')
    i += 1
