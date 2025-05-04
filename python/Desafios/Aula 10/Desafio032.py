import calendar

#Entrada de dados via teclado com o tipo inteiro e validada
liberado = False
while liberado == False:
    ano = int(input('Digite o ano: '))
    if ano <= 0:
        print('Ano inválido! Tente novamente!')
    else:
        liberado = True

#Verificação da condição do ano ser bissexto
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print(f'O ano {ano} é bissexto.')
#else:
#    print(f'O ano {ano} não é bissexto.')

#Usando o módulo calendar
print(f'{ano} é bissexto' if calendar.isleap(ano) == True else f'{ano} não é bissexto.')
