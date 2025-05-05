from calendar import isleap
from datetime import datetime


#Entrada de dados via teclado com o tipo inteiro e validada
liberado = False
while liberado == False:
    ano = int(input('Digite o ano (coloque 0 para analisar o ano atual): '))
    if ano == 0:
        ano = datetime.now().year #Atribuo a o ano local à variável
        liberado = True
    if ano < 0:
        print(f'{'\033[4;31m'}Ano inválido!{'\033[m'} Tente novamente!')
    else:
        liberado = True

#Verificação da condição do ano ser bissexto
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print(f'O ano {ano} é bissexto.')
#else:
#    print(f'O ano {ano} não é bissexto.')

#Usando o módulo calendar
print(f'{ano} {'\033[0;34m'}é bissexto{'\033[m'}' if isleap(ano) == True else f'{ano} {'\033[0;31m'}não é bissexto{'\033[m'}.')
