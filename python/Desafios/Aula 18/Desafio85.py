#Função para validar entrada de inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro! Tente novamente!\033[m {e}')


#Entrada e processamento de dados
numeros = [[], []] #índice 0 são pares e índice 1 são ímpares

for i in range(7):
    valor = valida_inteiros(f'Digite o {i + 1}º valor: ')
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)


#Apresentação do resultado
print('-' * 40)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
