#Função para validar a entrada de dados
def valida_entrada(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0 or numero > 20: #Regra de negócio
                raise ValueError('Valor inválido!')
            return numero
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mO número precisa estar entre 0 e 20!\033[m {e}')
            else:
                print(f'\033[0;91mDado informado não é do tipo inteiro!\033[m {e}')


#Função para validar a resposta do usuário quanto à continuidade do loop principal
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).upper()
            if resposta != 'S' and resposta != 'N': #Regra de negócio
                raise ValueError('Tente novamente!')
            return resposta
        except ValueError as e:
            if 'Tente novamente!' in str(e):
                print(f'\033[0;91mDigite S para Sim e N para Não!\033[m {e}')


#Inicialização da tupla
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
         'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#Lógica principal com a chamada da função de validação de entrada
while True:
    num = valida_entrada('Digite um número entre 0 e 20: ')
    print(f'Você digitou o número {tupla[num]}')
    continuar = valida_resposta('Deseja continuar? [S/N] ')
    if continuar == 'N':
        break
