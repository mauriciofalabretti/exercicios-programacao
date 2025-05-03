#Entrada de dados através do teclado com o tipo inteiro
numero = int(input('Informe um número inteiro: '))

#Condicional que verifica se o número é par ou ímpar
print(f'O número {numero} é PAR!' if numero % 2 == 0 else f'O número {numero} é ÍMPAR!')