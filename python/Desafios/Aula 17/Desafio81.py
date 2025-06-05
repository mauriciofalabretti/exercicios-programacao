#Função para validar entrada de inteiros
def valida_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente! {e}')


#Função para validar resposta do usuário
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).strip().upper()
            if resposta != 'S' and resposta != 'N': #Regra de negócio
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError as e:
            if 'Resposta inválida!' in str(e):
                print(f'\033[0;91mDigite S para Sim ou N para Não!\033[m {e}')


#Programa principal com loop para entrada de dados até o usuário desejar
numeros = list()
cont = 0
while True:
    numeros.append(valida_inteiro('Digite um valor: '))
    continua = valida_resposta('Deseja continuar? [S/N] ')
    cont += 1
    if continua == 'N':
        break

#Apresentação dos resultados
print('-' * 30)
print(f'Você digitou {cont} elementos')
print(f'Os valores da lista em ordem decrescente {sorted(numeros, reverse=True)}')
print('O valor 5 faz parte da lista!' if 5 in numeros else 'O valor 5 não faz parte da lista!')
