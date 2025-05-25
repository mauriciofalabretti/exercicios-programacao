#Declaração da tupla contendo os times do campeonato brasileiro por ordem de classificação
campeonato = ('Palmeiras', 'Flamengo', 'Bragantino', 'Cruzeiro', 'Fluminense',
              'Ceará SC', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians',
              'Fortaleza', 'Mirassol', 'Internacional', 'EC Vitória', 'Grêmio',
              'São Paulo', 'Vasco da Gama', 'Juventude', 'Santos', 'Sport Recife')

#Mostra os cinco primeiros colocados
print('-' * 30)
print(f'Os 5 primeiros colocados são: {campeonato[:5]}')
print('-' * 30)
#Mostra os últimos quatro colocados
print(f'Os últimos 4 colocados são: {campeonato[-4:]}')
print('-' * 30)
#Mostra a uma lista com os times ordenados em ordem alfabética
print(f'Times em ordem alfabética: {sorted(campeonato)}')
print('-' * 30)
#Mostra a posição na tabela em que está o time do Mirassol
print(f'O Mirassol está na {campeonato.index('Mirassol') + 1}ª colocação')

