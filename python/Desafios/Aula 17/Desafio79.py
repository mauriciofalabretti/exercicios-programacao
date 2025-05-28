#Função para validar entrada de números inteiros
def valida_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = (int(input(mensagem)))
            return numero
        except ValueError as e:
            print(f'\033[0;91mO número precisa ser do tipo inteiro!\033[m Tente novamente! {e}')


#Função para validar a resposta que ativa o flag
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).upper().strip()
            if resposta != 'S' and resposta != 'N':
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError as e:
            if 'Resposta inválida!' in str(e):
                print(f'\033[0;91mInforme S para Sim ou N para Não!\033[m {e}')


#Declaração da lista, loop infinito com flag de controle, entrada de valores
lista = list()
while True:
    valor = valida_inteiro('Digite um valor: ')
    if valor in lista: #Condicional verifica se o número já foi digitado
        print('Valor duplicado! Não será adicionado...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continua = valida_resposta('Deseja continuar? [S/N] ')
    if continua == 'N':
        break


#Apresentação dos dados após o processamento
print('-' * 30)
print(f'Os valores informados foram: {sorted(lista)}')
