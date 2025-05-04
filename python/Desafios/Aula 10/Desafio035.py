#Entrada de dados com o tipo float recebendo as retas de um triângulo
##Função para validar as medidas
def valida_medidas(mensagem):
    while True:
        try:
            medida = float(input(mensagem))
            if medida <= 0:
                raise ValueError('MenorIgualZero')
            return medida
        except ValueError as e:
            if 'MenorIgualZero' in str(e):
                print('Medida não pode ser igual ou menor à zero!')
            else:
                print(f'ERRO! Valor inserido é inválido! {e}')
        except Exception as e:
            print(f'Erro inesperado! {e}')

r1 = valida_medidas('Informe a primeira reta: ')
r2 = valida_medidas('Informe a segunda reta: ')
r3 = valida_medidas('Informe a terceira reta: ')

#Verificação da condição de existência de um triângulo
permitido = False
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas formam um triângulo!\n')
    permitido = True
else:
    print('As retas não formam um triângulo!')

#Verifica o tipo do triângulo
if permitido == True:
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓSCELES')
