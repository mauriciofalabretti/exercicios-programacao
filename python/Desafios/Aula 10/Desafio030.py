#Entrada de dados através do teclado com o tipo inteiro
numero = int(input('Informe um número inteiro: '))

#Condicional que verifica se o número é par ou ímpar
print(f'O número {numero} é {'\033[1;96m'}PAR{'\033[m'}!' if numero % 2 == 0 else f'O número {numero} é {'\033[1;91m'}ÍMPAR{'\033[m'}!')