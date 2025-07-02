from random import randint
from time import sleep

#Função para sortear os valores de uma lista
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(1)
    print('Pronto!')


#Função para somar os valores pares de uma lista
def soma_par(lista):
    tot_par = 0
    for v in lista:
        if v % 2 == 0:
            tot_par += v
    print(f'Somando os valores pares de {lista}, temos {tot_par}')


# Programa Principal
numeros = list()
sorteia(numeros)
soma_par(numeros)
