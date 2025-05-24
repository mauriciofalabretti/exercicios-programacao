from random import randint

#Função para validar entrada de inteiros
def valida_inteiros(mensagem: str) -> int:
    '''função verifica se a regra de negócio não foi violada e se o tipo da entrada é inteira'''
    alternativas = {1, 2}
    while True:
        try:
            n = int(input(mensagem))
            if n not in alternativas: #Regra de Negócio
                raise ValueError('Opção inválida!')
            return n
        except ValueError as e:
            if 'Opção inválida!' in str(e):
                print(f'\033[0;91mDigite 1 ou 2!\033[m {e}')
            else:
                print(f'\033[0;91mValor precisa ser do tipo inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função para validar entrada string
def valida_string(mensagem: str) -> str:
    '''função verifica se o usuário escolheu uma opção inválida e se o dado inserido é string'''
    while True:
        try:
            s = str(input(mensagem)).strip().upper()
            if s != 'P' and s != 'I': #Regra de Negócio
                raise ValueError('Opção inválida!')
            if s.isdigit(): #Regra de Negócio
                raise ValueError('Tipo inválido!')
            return s
        except ValueError as e:
            if 'Opção inválida!' in str(e):
                print(f'\033[0;91mEscolha P para Par ou I para Ímpar!\033[m {e}')
            elif 'Tipo inválido!' in str(e):
                print(f'\033[0;91mDado digitado precisa ser uma letra!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Lógica principal com loop de jogadas
cont_vit = 0
while True:
    comp_numero = randint(1, 2)
    jogador_jogada = valida_string('\033[0;34m(P) Par\033[m ou \033[0;33m(I) Ímpar?\033[m ')
    jogador_numero = valida_inteiros('\033[0;95mJogue 1 ou 2:\033[m ')
    if 'P' in jogador_jogada:
        if jogador_numero != comp_numero:
            break
    else:
       if jogador_numero == comp_numero:
           break
    print(f'\033[0;96mVitória!\033[m Você escolheu \033[7;94;40m{jogador_jogada}\033[m e o computador jogou \033[7;94;40m{comp_numero}\033[m')
    cont_vit += 1

#Apresentação dos resultados
if cont_vit == 0:
    print(f'\033[0;91mDerrota...\033[mVocê escolheu \033[7;94;40m{jogador_jogada}\033[m e o computador jogou \033[7;94;40m{comp_numero}\033[m')
else:
    print(f'\033[0;91mDerrota...\033[mVocê escolheu \033[7;94;40m{jogador_jogada}\033[m e o computador jogou \033[7;94;40m{comp_numero}\033[m\n'
          f'\033[m Você venceu \033[0;95m{cont_vit}\033[m rodadas consecutivas!')
