#Função para validar nome
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            name = str(input(mensagem)).strip()
            if name.isdigit == True:
                raise ValueError('Nome inválido!')
            elif len(name) == 0:
                raise ValueError('Campo vazio!')
            return name
        except ValueError as e:
            if 'Nome inválido!' in str(e):
                print(f'\033[0;91mNome não pode conter dígitos!\033[m Tente novamente!')
            elif 'Campo vazio!':
                print(f'\033[0;91mNome não pode ficar vazio!\033[m')


#Função para validar peso
def valida_peso(mensagem: str) -> float:
    while True:
        try:
            pe = float(input(mensagem))
            if pe <= 0.9: #Regra de negócio
                raise ValueError('Valor inválido!')
            return pe
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mPeso deve ser maior que zero!\033[m {e}')
            else:
                print(f'\033[0;91mDigite um peso válido!\033[m {e}')


#Entrada de dados
pessoas = list()
dados = list()
cont_pessoas = 0
while True:
    dados.append(valida_nome('Digite o seu nome: '))
    dados.append(valida_peso('Digite o seu peso: '))
    pessoas.append(dados[:])
    dados.clear()
    cont_pessoas += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break


#Lógica para encontrar o maior e menor peso
maior_peso = None
menor_peso = None
cont = 0
for p in pessoas:
    if cont == 0:
        maior_peso = p[1]
        menor_peso = p[1]
    else:
        if p[1] > maior_peso:
            maior_peso = p[1]
        elif p[1] < menor_peso:
            menor_peso = p[1]
    cont += 1


#lógica para encontrar as pessoas com os maiores e menores pesos
mais_pesado = []
menos_pesado = []

for p in pessoas:
    if maior_peso == p[1]:
        mais_pesado.append(p[0])
    if menor_peso == p[1]:
        menos_pesado.append(p[0])


#Apresentação dos resultados
print(pessoas)
print(f'Foram cadastradas {cont_pessoas} pessoas')
print(f'O maior peso registrado foi {maior_peso} kg. Peso de', end=' ')
for nome in mais_pesado:
    print(f'[{nome}]', end=' ')
print(f'\nO menor peso registrado foi {menor_peso} kg. Peso de', end=' ')
for nome in menos_pesado:
    print(f'[{nome}]', end=' ')
