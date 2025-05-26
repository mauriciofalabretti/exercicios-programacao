#Função para validar entradas do tipo inteiro
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mNúmero do tipo inteiro!\033[m {e}')


#Função para contar ocorrências de números pares em uma tupla
def conta_pares(tupla: tuple) -> int:
    cont = 0
    for item in tupla:
        if item % 2 == 0:
            cont += 1
    return cont


#Programa principal
valores = (valida_inteiros('Digite um número: '), valida_inteiros('Digite outro número: '),
           valida_inteiros('Digite mais um número: '), valida_inteiros('Digite o último número: '))

#Apresentação dos resultados
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if valores.count(3) > 0: #Condicional para verificar a ocorrência do número 3
    print(f'O valor 3 apareceu primeiro na {valores.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

#Inicializa o contador de números
contador = conta_pares(valores)

#Se houver números pares na tupla, então eles serão apresentados
if contador > 0:
    print(f'Os valores pares digitados foram', end=' ')
    for i in valores:
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('Não foram informados valores pares')
