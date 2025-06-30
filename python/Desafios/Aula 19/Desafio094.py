import statistics
import re

#Função para validar o nome
def valida_nome(mensagem: str) -> str:
    while True:
        try:
            name = str(input(mensagem)).strip()
            if re.search(r'\d', name) or len(name) == 0:
                raise ValueError('Nome inválido!')
            return name
        except ValueError:
            print(f'\033[0;91mNome não pode ser vazio ou conter números!\033[m Tente novamente!')

#Função para validar o sexo
def valida_sexo(mensagem: str) -> str:
    while True:
        try:
            se = str(input(mensagem)).strip().upper()[0]
            if se != 'M' and se != 'F':
                raise ValueError('Opção inválida!')
            return se
        except ValueError as e:
            print(f'\033[0;91mDigite M para Masculino ou F para Feminino!\033[m Tente novamente! {e}')

#Função para validar a idade
def valida_idade(mensagem: str) -> int:
    while True:
        try:
            idades = int(input(mensagem))
            if idades <= 0:
                raise ValueError('Idade inválida!')
            return idades
        except ValueError as e:
            if 'Idade inválida!' in str(e):
                print(f'\033[0;91mIdade deve ser maior que zero!\033[m Tente novamente!')
            else:
                print(f'\033[0;91mIdade deve ser um número inteiro!\033[m Tente novamente! {e}')

#Função para validar a resposta
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).strip().upper()[0]
            if resposta != 'S' and resposta != 'N':
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError:
            print(f'\033[0;91mDigite S para Sim ou N para Não!\033[m Tente novamente!')

if __name__ == '__main__':
    #Entrada de dados
    pessoas = dict()
    lista_pessoas = list()
    while True: #Loop para preenchimento do dicionário e lista
        pessoas = {
            'nome': valida_nome('Nome: '),
            'sexo': valida_sexo('[M/F]: '),
            'idade': valida_idade('Idade: ')
        }
        lista_pessoas.append(pessoas.copy())
        continuar = valida_resposta('Deseja continuar? [S/N] ')
        if continuar == 'N':
            print('Saindo...')
            break

    #Processamento de dados
    media_idades = statistics.mean([pessoa['idade'] for pessoa in lista_pessoas]) #Função com list comprehension para a média
    #total_mulheres = sum([1 for pessoa in lista_pessoas if pessoa['sexo'] == 'F'])
    mulheres = list()
    for pessoa in lista_pessoas:
        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa)

    '''idade_acima_media = list()
    for pessoa in lista_pessoas:
        if pessoa['idade'] > media_idades:
            idade_acima_media.append(pessoa)'''

    #Saída de dados, apresentação dos resultados
    print('-' * 50)
    print(f'- Foram cadastradas {len(lista_pessoas)} pessoas.')
    print(f'- A média de idade do grupo é {media_idades:.2f} anos.')
    print('- Lista das mulheres cadastradas:')
    for mulher in mulheres:
        print(f'[{mulher['nome']}]', end=' ')

    print(f'\n- Pessoas com idade acima da média:')
    for k, v in pessoas.items():
        print(f'[{k} = {v}];', end=' ')

print(f'\n{' ENCERRADO ':-^40}')
