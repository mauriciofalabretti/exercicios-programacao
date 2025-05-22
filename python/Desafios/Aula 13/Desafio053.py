#Função para validar strings
def valida_string(mensagem: str) -> str:
    while True:
        try:
            s = str(input(mensagem))
            if s.isdigit() == True:
                raise ValueError('Tipo inválido!')
            return s
        except ValueError as e:
            if 'Tipo inválido!' in str(e):
                print(f'\033[0;91mA entrada deve ser uma string!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Entrada de dados
frase_original = valida_string('Digite uma frase: ').strip() #Elimino os espaços no início e fim da string
frase = frase_original #Transfiro a frase original para uma variável que vai manipulá-la
lista = frase.split() #Separa a string em pedaços, eliminando os espaços entre as palavras, que vão compor a lista auxiliar
frase = ''.join(lista).upper() #Junta os itens da lista e atribui de volta à variável, dessa vez sem espaços internos
aux_invertida = [*frase] #Variável auxiliar atuando como lista para armazenar os caracteres individualmente da frase
aux_invertida.reverse() #Inverte a ordem dos caracteres dentro da lista
frase_invertida = ''.join(aux_invertida) #Entrega e une os caracteres já invertidos para a variável específica

#Mostra a frase invertida
print(f'O inverso de {frase} é {frase_invertida}')

#Lógica de verificação de palíndromos
cont = 0
for i in range(0, len(frase)): #Loop que verifica letra por letra se são iguais em posições equidistantes
    if frase[i] == frase[len(frase) - (i + 1)]:
        cont += 1

#Condicional que verifica se a frase é um palíndromo
if cont == len(frase):
    print(f'\033[0;92mA frase {frase_original} é um palíndromo!\033[m')
else:
    print(f'\033[0;31mA frase {frase_original} não é um palíndromo!\033[m')
