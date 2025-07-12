#Função para validar a entrada de anos
def valida_ano(mensagem: str) -> int:
    while True:
        try:
            ano = int(input(mensagem))
            if len(str(ano)) != 4 or ano < 0:
                raise ValueError('Ano inválido!')
            return ano
        except ValueError as e:
            if 'Ano inválido!' in str(e):
                print(f'\033[0;91mAno deve conter 4 dígitos e ser maior positivo!\033[m Tente novamente!')
            else:
                print(f'\033[0;91mAno deve ser um valor do tipo inteiro!\033[m Tente novamente!')

if __name__ == '__main__':
    # Função para verificar se a pessoa deve votar
    def voto(nascimento):
        from datetime import date as dt
        idade = dt.today().year - nascimento
        if idade >= 18 and idade <= 65:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO'
        elif (idade >= 16 and idade < 18) or idade > 65:
            return f'Com {idade} anos: VOTO OPCIONAL'
        else:
            return f'Com {idade} anos: NÃO VOTA'


    # Programa Principal
    print('-' * 30)
    ano_nasc = valida_ano('Em que ano você nasceu? ')
    print(voto(ano_nasc))
