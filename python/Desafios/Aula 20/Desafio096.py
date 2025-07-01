def valida_float(mensagem: str) -> float:
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print(f'\033[0;91mErro! Valor deve ser do tipo float!\033[m Tente novamente!')


def calc_area(larg, comp: float):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area:.1f}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 22)
largura = valida_float('Largura (m): ')
comprimento = valida_float('Comprimento (m): ')
calc_area(largura, comprimento)
