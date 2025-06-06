#Função para validar a entrada de inteiros
def valida_int(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente! {e}')


#Função para validar a respota do usuário
def valida_resp(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).strip().upper()
            if resposta != 'S' and resposta != 'N': #Regra de negócio
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError as e:
            if 'Resposta inválida!' in str(e):
                print(f'\033[0;91mDigite S para Sim e N para Não!\033[m {e}')


#Loop para entrada de dados
numeros = list()
while True:
    numeros.append(valida_int('Digite um número: '))
    continua = valida_resp('Deseja continuar? [S/N] ')
    if continua == 'N':
        break


#Loop para verificar números pares e ímpares
pares = list()
impares = list()
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

#Apresentação das listas
print('-' * 30)
print(f'Lista completa {numeros}')
print(f'Lista de pares {pares}')
print(f'Lista de ímpares {impares}')
