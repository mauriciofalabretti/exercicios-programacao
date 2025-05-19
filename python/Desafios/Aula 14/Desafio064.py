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


#Loop para a entrada de valores e seu processamento
num = 0
soma = 0
cont = 0
while num != 999:
    num = valida_inteiros('Digite um número (ou [999] para parar): ')
    if num != 999:
        soma += num
        cont += 1

#Apresentação dos resultados
print(f'\nForam digitados \033[0;94m{cont} números\033[m ao todo')
print(f'A soma entre eles é \033[0;94m{soma}\033[m')
