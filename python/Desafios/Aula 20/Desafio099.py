from time import sleep

def maior(* numeros):
    print('-' * 50)
    print('Analisando os valores passados...')
    for i in numeros:
        print(i, end=' ')
        sleep(1)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    if len(numeros) != 0:
        print(f'O maior valor informado foi {max(numeros)}.')
    else:
        print(f'O maior valor informado foi 0.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
