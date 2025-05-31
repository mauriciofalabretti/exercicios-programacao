#Função para validar o saque
def valida_saque(mensagem: str) -> int:
    while True:
        try:
            saque = int(input(mensagem))
            if saque <= 0: #Regra de negócio
                raise ValueError('Saque inválido!')
            return saque
        except ValueError as e:
            if 'Saque inválido!' in str(e):
                print(f'\033[0;91mValor precisa ser maior que zero!\033[m {e}')
            else:
                print(f'\033[0;91mDigite um valor inteiro!\033[m {e}')


#Função para calcular a quantidade de notas
def calcula_qtd_notas(saque, cedula: int) -> int:
    return saque // cedula


#Função para calcular o valor formado pelas notas
def calcula_valor_notas(qtd_notas, cedula: int) -> int:
    return qtd_notas * cedula


#Lógica principal contendo loop que verifica a quantidade de cédulas que compõem o saque
cedulas = [50, 20, 10, 1]

while True:
    #Cria a interface
    print('=' * 30)
    print(f'{f' ORIGINAL BANK ':-^30}')
    print('=' * 30)
    valor_saque = valida_saque('Valor do Saque: R$ ')
    valor_original = valor_saque #Preserva o valor do saque
    #Cédulas de R$ 50
    qtd_notas_50 = calcula_qtd_notas(valor_saque, cedulas[0])
    valor_em_50 = calcula_valor_notas(qtd_notas_50, cedulas[0])
    valor_saque -= valor_em_50
    #Cédulas de R$ 20
    qtd_notas_20 = calcula_qtd_notas(valor_saque, cedulas[1])
    valor_em_20 = calcula_valor_notas(qtd_notas_20, cedulas[1])
    valor_saque -= valor_em_20
    #Cédulas de R$ 10
    qtd_notas_10 = calcula_qtd_notas(valor_saque, cedulas[2])
    valor_em_10 = calcula_valor_notas(qtd_notas_10, cedulas[2])
    valor_saque -= valor_em_10
    #Cédulas de R$ 1
    qtd_notas_1 = calcula_qtd_notas(valor_saque, cedulas[3])
    valor_em_1 = calcula_valor_notas(qtd_notas_1, cedulas[3])
    valor_saque -= valor_em_1
    break


#Apresentação de resultado
print(f'\nSeu saque foi de \033[0;35mR$ {valor_original:.2f}\033[m e você recebeu:')
if valor_em_50 > 0:
    print(f'Total de \033[0;35m{qtd_notas_50}\033[m cédulas de \033[0;35mR$ 50\033[m')
if valor_em_20 > 0:
    print(f'Total de \033[0;35m{qtd_notas_20}\033[m cédulas de \033[0;35mR$ 20\033[m')
if valor_em_10 > 0:
    print(f'Total de \033[0;35m{qtd_notas_10}\033[m cédulas de \033[0;35mR$ 10\033[m')
if valor_em_1 > 0:
    print(f'Total de \033[0;35m{qtd_notas_1}\033[m cédulas de \033[0;35mR$ 1\033[m')
print('=' * 30)
print(f'Volte sempre ao ORIGINAL BANK! Tenha um bom dia!')
