from datetime import datetime
import re

#Função para validar o nome
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            nome = str(input(mensagem)).strip()
            nome = nome.replace(" ", "")
            if re.search(r'\d', nome) or len(nome) == 0: #Regra de negócio
                raise ValueError('Nome inválido!')
            return nome
        except ValueError as e:
            print(f'\033[0;91mNome não pode ser vazio ou conter números!\033[m Tente novamente! {e}')

#Função para validar o ano
def valida_ano(mensagem: str) -> int:
    while True:
        try:
            ano = int(input(mensagem))
            if ano <= 0: #Regra de negócio
                raise ValueError('Ano inválido!')
            return ano
        except ValueError as e:
            if 'Ano inválido!' in str(e):
                print(f'\033[0;91mAno deve ser maior que zero!\033[m Tente novamente! {e}')
            else:
                print(f'\033[0;91mAno deve ser um valor inteiro!\033[m Tente novamente! {e}')

#Função para validar o salário
def valida_salario(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0: #Regra de negócio
                raise ValueError('Valor inválido!')
            return valor
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mSalário deve ser maior que zero!\033[m Tente novamente! {e}')
            else:
                print(f'\033[0;91mSalário deve ser um valor numérico!\033[m Tente novamente! {e}')

#Função para validar a carteira
def valida_ctps(mensagem: str) -> int:
    while True:
        try:
            carteira = int(input(mensagem))
            if carteira < 0:
                raise ValueError('Número inválido!')
            return carteira
        except ValueError as e:
            if 'Número inválido!' in str(e):
                print(f'\033[0;91mNúmero não pode ser menor que zero!\033[m Tente novamente! {e}')
            else:
                print(f'\033[0;91mDigite um número inteiro válido!\033[m Tente novamente! {e}')

if __name__ == '__main__':
    #Inicializa e preenche o dicionário com a entrada de dados
    trabalhador = {
            'nome' : valida_nome('Nome: '),
            'idade' : datetime.now().year - valida_ano('Ano de Nascimento: '),
            'ctps' : valida_ctps('Carteira de Trabalho: (0 não tem): ')
        }

    if trabalhador['ctps'] != 0: #Verifica se o usuário tem carteira e adiciona itens em caso positivo
        trabalhador['contratacao'] = valida_ano('Ano de contratação: ')
        trabalhador['salario'] = valida_salario('Salário: R$ ')

    #Apresenta os dados do dicionário utilizando um loop
    print('-' * 50)
    print(trabalhador)
    for k, v in trabalhador.items():
        print(f'{k} tem o valor {v}')

    if 'contratacao' in trabalhador:
        idade_ctps = datetime.now().year - trabalhador['contratacao'] #Calcula há quanto tempo o usuário assinou a carteira
        aposentar = 35 - idade_ctps #Calcula a diferença de 35 anos para o tempo de carteira assinada
        print(f'aposentadoria tem o valor {trabalhador['idade'] + aposentar}') #Apresenta a idade em que o usuário deve se aposentar
