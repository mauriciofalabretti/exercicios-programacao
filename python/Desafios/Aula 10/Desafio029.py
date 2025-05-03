#Entrada de dados através do teclado com o tipo float
velocidade = float(input('Informe a velocidade: '))

#Condicional verifica a aplicação de multa
if velocidade > 80:
    valor_multa = (velocidade - 80) * 7 #Encontro o excesso de velocidade e calculo o valor da multa pelo valor de R$ 7,00
    print(f'Velocidade acima dos 80 Km/h permitidos!\n'
          f'Você foi multado em: R$ {valor_multa:.2f}')
else:
    print('Velocidade dentro do permitido.')