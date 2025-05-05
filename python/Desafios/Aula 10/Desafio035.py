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
                print(F'{'\033[3;91;107m'}Medida não pode ser igual ou menor à zero!{'\033[m'}')
            else:
                print(f'{'\033[3;91;107m'}ERRO! Valor inserido é inválido!{'\033[m'} {e}')
        except Exception as e:
            print(f'{'\033[3;91;107m'}Erro inesperado!{'\033[m'} {e}')

r1 = valida_medidas('Informe a primeira reta: ')
r2 = valida_medidas('Informe a segunda reta: ')
r3 = valida_medidas('Informe a terceira reta: ')

#Verificação da condição de existência de um triângulo
permitido = False
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'{'\033[1;92m'}As retas formam um triângulo!{'\033[m'}\n')
    permitido = True
else:
    print(f'{'\033[1;91m'}As retas não formam um triângulo!{'\033[m'}')

#Verifica o tipo do triângulo
if permitido == True:
    if r1 == r2 == r3:
        print(f'O triângulo é {'\033[1;94m'}EQUILÁTERO{'\033[m'}')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print(f'O triângulo é {'\033[1;95m'}ESCALENO{'\033[m'}')
    else:
        print(f'O triângulo é {'\033[1;93m'}ISÓSCELES{'\033[m'}')
