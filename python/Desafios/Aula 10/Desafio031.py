#Entrada e validação de dados pelo teclado com o tipo float
liberado = False
while liberado == False:
    distancia = float(input('Informe a distância da viagem em Km: '))
    if distancia <= 0:
        print('Distância não pode ser igual ou menor a zero!')
    else:
        liberado = True


#Condicional com o cálculo de preço da passagem baseado na distância da viagem
if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

print(f'Você irá pagar R$ {preco_passagem:.2f} pela passagem')