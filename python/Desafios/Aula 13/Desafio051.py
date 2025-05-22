#Função para validar entradas de inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mO tipo de dado inserido é inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados
primeiro_termo = valida_inteiros('Informe o primeiro termo da progressão aritmética: ')
razao = valida_inteiros('Informe a razão da progressão aritmética: ')

#Cálculo da parada considerando os 10 primeiros valores de uma progressão aritmética
#Como é conhecido o primeiro termo, multiplicamos os nove restantes pela razão e somamos ao primeiro para descobrir o termo final
#Munido do termo_final, sabendo que ele será excluído do for, criamos a parada e acrescentamos um ao termo final
termo_final = primeiro_termo + (10 - 1) * razao
parada = termo_final + 1

#Execução e apresentação da progressão aritmética
for i in range(primeiro_termo, parada, razao):
    print(f'| {i} ', end='')

print('|')
