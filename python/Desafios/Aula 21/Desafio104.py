# Função para validar entrada de inteiros
def leia_int(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('\033[0;91mERRO! Digite um número inteiro válido\033[m')


# Programa Principal
num = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
