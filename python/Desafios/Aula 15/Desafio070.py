#Função para validar a resposta do usuário quanto à continuidade do loop
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            r = str(input(mensagem)).strip().upper()
            if 'S' != r != 'N': #Regra de negócio
                raise ValueError('Digite uma letra!')
            return r
        except ValueError as e:
            print(f'\033[0;91mResponda S para Sim ou N para Não!\033[m {e}')


#Função para validar o preço do produto
def valida_preco(mensagem: str) -> float:
    while True:
        try:
            p = float(input(mensagem))
            if p <= 0: #Regra de negócio
                raise ValueError('Digite um valor maior!')
            return p
        except ValueError as e:
            if 'Digite um valor maior!' in str(e):
                print(f'\033[0;91mO preço não pode ser igual ou menor que zero!\033[m {e}')
            else:
                print(f'\033[0;91mDigite um valor do tipo válido!\033[m {e}')


#Função para validar o nome do produto
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            no = str(input(mensagem)).strip().split()
            novonome = ''.join(no) #Para o caso do nome ser alfanumérico e conter espaço interno
            if novonome.isdigit() or novonome.isalnum() == False: #Regra de negócio
                raise ValueError('Nome inválido!')
            elif len(no) == 0: #Regra de negócio
                raise ValueError('Insira um nome!')
            return novonome
        except ValueError as e:
            if 'Nome inválido!' in str(e):
                print(f'\033[0;91mNome não deve ser formado apenas por números!\033[m {e}')
            elif 'Insira um nome!' in str(e):
                print(f'\033[0;91mCampo não pode ser deixado em branco!\033[m {e}')


#Função verifica e retorna 1 se o valor passado como argumento for superior à R$ 1000.00
def acima_de_mil(valor: float) -> int:
    contador = 0
    if valor > 1000:
        contador += 1
    return contador


#Função verifica e retorna qual é o nome e o valor do produto mais barato cadastrado
def produto_mais_barato(lista_atual: list, nome_produto:str, valor_produto: float) -> list:
    if valor_produto < lista_atual[1]:
         lista_atual[0] = nome_produto
         lista_atual[1] = valor_produto
    return lista_atual


#Programa principal com inicialização de variáveis e loop de cadastro
total_gasto = 0
qtd_mais_de_mil = 0
mais_barato = [None] * 2
cont = 0

print(f'{f' LOJA ':=^30}')
while True:
    nome = valida_nome('Nome do produto: ')
    preco = valida_preco('Preço do produto: R$ ')
    total_gasto += preco
    qtd_mais_de_mil += acima_de_mil(preco)

    if cont == 0:
        mais_barato[0] = nome
        mais_barato[1] = preco
    else:
        mais_barato = produto_mais_barato(mais_barato, nome, preco)

    cont += 1
    continuar = valida_resposta('Quer continuar? [S/N] ')
    if continuar == 'N':
        break


#Apresentação de resultados
print(f'\033[0;94m{f' NOTA DE COMPRA ':#^30}\033[m')
print(f'\033[0;34mTotal de itens:\033[m {cont} itens')
print(f'\033[0;34mTotal gasto:\033[m R$ {total_gasto:.2f}')
print(f'\033[0;34mProdutos acima de R$ 1000.00:\033[m {qtd_mais_de_mil} produtos')
print(f'\033[0;34mProduto mais barato:\033[m {mais_barato[0]}, custando R$ {mais_barato[1]:.2f}')
