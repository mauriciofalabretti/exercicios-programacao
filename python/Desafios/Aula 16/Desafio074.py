from random import randint

#Tupla com valores gerados aleatoriamente
numero = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10))

#Apresentação dos resultados
print(f'Os valores sorteados foram: ', end='')
for n in numero:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')
