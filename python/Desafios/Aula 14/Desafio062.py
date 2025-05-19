#Função para validação de entradas do tipo inteiro
def valida_inteiros(mensagem: str) -> int:
    while True:
        try:
            n = int(input(mensagem))
            if 'continuar' in mensagem:
                if n < 0:
                    raise ValueError('Opção inválida!')
            return n
        except ValueError as e:
            if 'Opção inválida!' in str(e):
                print(f'\033[0;91mNúmero não pode ser negativo!\033[m {e}')
            else:
                print(f'\033[0;91mDado inserido precisa ser um número inteiro!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado!\033[m {e}')


#Função que verifica se o usuário deseja continuar
def usuario_continua() -> int:
    c = valida_inteiros(f'\nDeseja continuar? \n'
                        f'Se sim, informe quantos termos adicionais deseja, ou\n'
                        f'caso queira sair, digite (\033[0;93m0\033[m):\n')
    return c


#Entrada de dados
primeiro_termo = valida_inteiros('Informe o primeiro termo: ')
razao = valida_inteiros('Informe a razão: ')

print(f'[\033[0;94m{primeiro_termo}\033[m]', end=' ')
i = 1
#Loop inicial com os primeiros dez termos de uma progressão aritmética
while i <= 9:
    primeiro_termo += razao #Atualiza o primeiro termo a cada iteração
    print(f'[\033[0;94m{primeiro_termo}\033[m]', end=' ')
    i += 1

#Loop adicional que verifica se o usuário deseja continuar
continua = 1
termos = 0
while continua != 0:
    continua = usuario_continua()
    cont = 1
    if continua != 0:
        termos += continua
        while cont <= continua:
            primeiro_termo += razao
            print(f'[\033[0;94m{primeiro_termo}\033[m]', end=' ')
            cont += 1

print(f'A progressão aritmética foi finalizada com \033[0;33m{termos + 10}\033[m termos.')
