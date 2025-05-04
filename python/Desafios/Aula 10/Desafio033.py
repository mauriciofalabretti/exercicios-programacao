#Entrada de dados via teclado com o tipo inteiro e tratamento de erros

def validar_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError as e:
            print(f'Valor inserido não é do tipo inteiro!\n{e}')

n1 = validar_numero('Digite o primeiro número: ')
n2 = validar_numero('Digite o segundo número: ')
n3 = validar_numero('Digite o terceiro número: ')

#Verificando o número maior e o número menor (abordagem manual)
##Maior
'''maior = n1
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3

##Menor
menor = n1
if n2 < menor:
    menor = n2
elif n3 < menor:
    menor = n3

#Apresentação do maior e menor número
if n1 == n2 == n3:
    print('Os números são iguais!')
else:
    print(f'O número {maior} é o maior!')
    print(f'O número {menor} é o menor!')'''

#Verificando qual é o maior número e qual é o menor (abordagem simplificada)
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 == n2 == n3:
    print('Os números são iguais!')
else:
    print(f'O maior número é {maior}')
    print(f'O menor número é {menor}')

