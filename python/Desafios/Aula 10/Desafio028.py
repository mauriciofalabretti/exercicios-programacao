from random import randint
from time import sleep

#Sorteando um número inteiro entre 0 a 5
numero = randint(0, 5)

#Usuário tenta adivinhar o número sorteado e a variável armazena o valor inteiro
liberado = False
while liberado == False: #Loop para garantir o palpite dentro do intervalo válido
    palpite = int(input('Adivinhe o número sorteado entre 0 a 5: '))
    if palpite < 0 or palpite > 5: #Validação de entrada
        print('Valor inválido! Tente novamente!')
    else:
        liberado = True

#Efeito de pensamento
print('Sorteando o número...\n')
sleep(1)

#Condicional personaliza saída para o usuário de acordo com seu palpite
if palpite == numero:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena! Você errou...\n'
          f'O número sorteado foi {numero}.')