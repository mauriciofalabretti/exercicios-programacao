#Função para validar o tipo da entrada como inteiro
def valida_numero(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if n <= 0:
                raise ValueError('Opção Inválida!')
            return n
        except ValueError as e:
            if 'Opção Inválida!' in str(e):
                print(f'\033[0;91mValor menor ou igual a zero!\033[m {e}')
            else:
                print(f'\033[0;91mValor inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')

#Entrada de dados com o usuário escolhendo a opção desejada
tabuada = valida_numero('Informe o número que deseja ver a tabuada: ')

print(f'\033[0;30;47m{' TABUADA ':-^20s}\033[m')

#Executa e mostra a tabuada escolhida pelo usuário
for i in range(1, 11):
    print(f'\033[0;96m{tabuada} x {i} = {tabuada * i}')
