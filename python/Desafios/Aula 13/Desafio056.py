#Função para validar entrada de dados do tipo inteiro
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if n <= 0: #Regra de negócio
                raise ValueError('Valor inválido!')
            return n
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mValor deve ser superior à zero!\033[m {e}')
            else:
                print(f'\033[0;91mDado inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para validar entrada do tipo string
def valida_string(mensagem: str) -> str:
    while True:
        try:
            s = str(input(mensagem)).strip()
            if len(s) == 0 or s.isdigit(): #Regra de negócio
                raise ValueError('Entrada inválida!')
            return s
        except ValueError as e:
            if 'Entrada inválida!' in str(e):
                print(f'\033[0;91mDado inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função validar a entrada do sexo
def valida_sexo(mensagem: str) -> str:
    lista = {'M', 'F'} #Lista com os valores aceitos
    while True:
        try:
            s = str(input(mensagem)).upper().strip()
            if s not in lista: #Regra de negócio
                raise ValueError('Entrada inválida!')
            elif s.isdigit():
                raise ValueError('Deve ser string!')
            return s
        except ValueError as e:
            if 'Entrada inválida' in str(e):
                print(f'\033[0;91mDigite "M/m" para Masculino ou "F/f" para Feminino!\033[m {e}')
            elif 'Deve ser string!' in str(e):
                print(f'\033[0;91mDado inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Inicialização das variáveis utilizadas dentro do loop
soma_idades = 0
homem_maisvelho = None
maior_idade = 0
qtd_mul_menosvinte = 0

for i in range (4): #Loop para entrada de dados e verificação de condições
    print(f"{f' {i + 1}ª Pessoa ':-^25}")
    nome = valida_string(f'Informe o nome: ')
    idade = valida_inteiros(f'Informe a idade: ')
    sexo = valida_sexo(f'Informe o sexo: [M/F] ')

    soma_idades += idade #Acumula as idades informadas
    if sexo == 'M': #Verifica se for do sexo masculino
        if idade > maior_idade: #Verifica se a idade é a maior registrada para um homem
            homem_maisvelho = nome
            maior_idade = idade

    if sexo == 'F': #Verifica se for do sexo feminino
        if idade < 20: #Verifica se a idade é menor que 20
            qtd_mul_menosvinte += 1


#Apresentação dos resultados
media_idades = soma_idades/4
print(f'\033[0;34mA média de idades é {media_idades:.1f} anos\033[m')
print(f'\033[0;34mO homem mais velho é {homem_maisvelho} com {maior_idade} anos\033[m')
print(f'\033[0;34mA quantidade de mulheres com menos de 20 anos é {qtd_mul_menosvinte}\033[m')
