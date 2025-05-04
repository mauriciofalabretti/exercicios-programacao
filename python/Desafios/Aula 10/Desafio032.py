from calendar import isleap
from datetime import datetime


#Entrada de dados via teclado com o tipo inteiro e validada
liberado = False
while liberado == False:
    ano = int(input('Digite o ano (coloque 0 para analisar o ano atual): '))
    if ano == 0:
        ano_atual = datetime.now() #Atribuo a data local completa na variável ano_atual
        ano = ano_atual.year #Acesso precisamente o ano através da variável ano_atual e atribuo ao ano
        liberado = True
    if ano < 0:
        print('Ano inválido! Tente novamente!')
    else:
        liberado = True

#Verificação da condição do ano ser bissexto
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print(f'O ano {ano} é bissexto.')
#else:
#    print(f'O ano {ano} não é bissexto.')

#Usando o módulo calendar
print(f'{ano} é bissexto' if isleap(ano) == True else f'{ano} não é bissexto.')
