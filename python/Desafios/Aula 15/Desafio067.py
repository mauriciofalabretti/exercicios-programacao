from time import sleep

#Função para validar inteiros
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError as e:
            print(f'\033[0;91mValor precisa ser um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Lógica principal com loop para tabuada
while True:
    tabuada = valida_inteiros('Digite a tabuada desejada (negativo para sair): ')
    if tabuada < 0:
        break
    print(f'\033[0;92m{f' TABUADA ':-^20}\033[m')
    cont = 1
    while cont <= 10:
        print(f'\033[0;94m{tabuada} x {cont} = {tabuada * cont}\033[m')
        cont += 1
    sleep(3)
