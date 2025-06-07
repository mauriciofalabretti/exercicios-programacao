#Função para validar a entrada de inteiros
def valida_int87(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro válido!\033[m Tente novamente! {e}')


#Criação da matriz com list comprehension
matriz = [[None for _ in range(3)] for _ in range(3)]

#Loop para preenchimento da matriz
for linha in range(len(matriz)):
    for elemento in range(len(matriz[linha])):
        matriz[linha][elemento] = valida_int87(f'Digite um valor para [{linha}][{elemento}]: ')

#Loop para apresentação da matriz e processamento de dados
soma_pares = 0
soma_ter_coluna = 0
print('-' * 35)
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(f'[ {matriz[linha][coluna]} ]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_ter_coluna += matriz[linha][coluna]
    print()

#Apresentação dos resultados
print('-' * 35)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_ter_coluna}')
print(f'O maior elemento da segunda linha é {max(matriz[1])}')
