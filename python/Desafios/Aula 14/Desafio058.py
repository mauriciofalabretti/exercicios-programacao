from random import randint

#Função para validar o palpite
def valida_palpite(mensagem: str) -> int:
    palpites = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #Coleção com os palpites permitidos
    while True:
        try:
            p = int(input(mensagem))
            if p not in palpites:
                raise ValueError('Palpite inválido!')
            return p
        except ValueError as e:
            if 'Palpite inválido!' in str(e):
                print(f'\033[0;91mVocê deve escolher um número de 0 a 10!\033[m {e}')
            else:
                print(f'\033[0;91mDado inserido não pode ser decimal, caractere ou lógico!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Lógica principal com o loop continuando enquanto o jogador não acertar o número sorteado
jogador = None
cont_jogadas = 0
computador = randint(0, 10)

print('Olá! Sou seu computador e vou sortear um número entre 0 e 10.\n'
      'Será que você consegue adivinhar?')

while jogador != computador:
    jogador = valida_palpite('Qual é o seu palpite? ')
    if jogador == computador:
        print(f'\033[0;92mParabéns! Você acertou!\033[m')
    elif jogador < computador:
        print('Mais... Tente outra vez')
    else:
        print('Menos... Tente de novo')
    cont_jogadas += 1

#Apresenta o número que foi sorteado e a quantidade de tentativas após o término do loop
print(f'O número sorteado foi \033[0;95m{computador}\033[m')
print(f'Você precisou de \033[0;95m{cont_jogadas}\033[m tentativas para acertar')
