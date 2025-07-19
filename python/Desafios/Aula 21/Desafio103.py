# Função para ficha do jogador
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
jogador = str(input('Nome do jogador: ')).strip()
qtd_gols = str(input('Número de gols: '))

## Verifica se o valor de qtd_gols é númerico e transforma para inteiro
if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0

## Verifica se o nome do jogador está vazio e chama a função adequando os parâmetros
if jogador.strip() == '':
    ficha(gols=qtd_gols)
else:
    ficha(jogador, qtd_gols)
