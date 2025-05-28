#Função para validar a entrada de inteiros
def valida_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor precisa ser do tipo inteiro!\033[m Tente novamente! {e}')


valores = list()

#Loop para entrada de cinco números
for i in range(5):
    valores.append(valida_inteiro(f'Digite o {i + 1}º valor: '))


#Apresenta a lista e seus valores máximo e mínimo, seguidos de seus respectivos índices
print(f'\nA lista: {valores}')
print(f'O maior valor é {max(valores)} ocupando as posições ', end='')
for pos, valor in enumerate(valores):
    if max(valores) == valor:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor é {min(valores)} ocupando as posições ', end='')
for pos, valor in enumerate(valores):
    if min(valores) == valor:
        print(f'{pos}...', end=' ')
