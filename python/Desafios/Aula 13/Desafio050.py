#Função para validar entrada de números inteiros
def valida_numeros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mValor inserido é do tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro Inesperado!\033[m {e}')

#Laço para verificação dos números pares durante as seis iterações
soma = 0 #Inicia a variável acumuladora
cont_par = 0 #Inicia a variável contadora
for i in range(1, 7):
    numero = valida_numeros(f'Digite o {i}º número: ')
    if numero % 2 == 0:
        soma += numero
        cont_par += 1

#Mostra o resultado da soma dos números pares informados
print(f'A soma dos \033[0;34m{cont_par}\033[m números pares informados é \033[0;34m{soma}\033[m.')
