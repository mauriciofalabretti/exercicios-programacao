#Função para validar entrada do tipo inteiro
def valida_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente! {e}')

if __name__=='__main__':
    #Criação da matriz 3 x 3 com list comprehension
    ##O primeiro for cria uma lista com três espaços vazios definidos
    ##O segundo for cria três listas com três espaços vazios cada
    matriz = [[None for _ in range(3)] for _ in range(3)]

    #Loop para preencher a matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = valida_inteiro(f'Digite o valor da posição [{i}][{j}]: ')

    #Loop para mostrar a matriz
    print('=' * 35)
    for i in matriz:
        for j in range(len(i)):
            print(f'[ {i[j]:^5} ]', end='')
        print()
