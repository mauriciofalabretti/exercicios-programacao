from time import sleep

#Função para validar entrada de inteiros
def valida_int(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente!')


#Função para contar valores
def contador(inicio, fim, passo: int):
    if passo < 0: #Verifica se o passo é negativo e transforma-o em positivo se for
        passo = passo * -1
        print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * - 1}')
    elif passo == 0: #Verifica se o passo é igual a zero e o transforma em 1
        passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim: #Concional para contagem crescente
        for n in range(i, f + 1, passo):
            print(f'{n} ', end='')
            sleep(1)
        print('FIM!')
    elif inicio > fim: #Condicional para contagem decrescente
        for n in range(i, f - 1, -passo):
            print(f'{n} ', end='')
            sleep(1)
        print('FIM!')


# Programa Principal
print('-' * 40)
print('Contagem de 1 até 10 de 1 em 1')
for i in range(1, 11):
    print(f'{i} ', end='')
    sleep(1)
print('FIM!')
print('-' * 40)
print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, -1, -2):
    print(f'{i} ', end='')
    sleep(1)
print('FIM!')
print('-' * 40)

print('Agora é sua vez de personalizar a contagem!')
i = valida_int('Inicio: ')
f = valida_int('Fim: ')
s = valida_int('Salto: ')
print('-' * 40)
contador(i, f, s)
