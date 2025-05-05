#Entrada e validação de dados pelo teclado com o tipo float
liberado = False
while liberado == False:
    distancia = float(input(f'Informe a distância da viagem em {'\033[1;95m'}Km{'\033[m'}: '))
    if distancia <= 0:
        print(f'Distância {'\033[1;91m'}não pode ser igual ou menor a zero!{'\033[m'}')
    else:
        liberado = True


#Condicional com o cálculo de preço da passagem baseado na distância da viagem
if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

print(f'Você irá pagar {'\033[7;36;107m'}R$ {preco_passagem:.2f}{'\033[m'} pela passagem')