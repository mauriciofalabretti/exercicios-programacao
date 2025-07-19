# Função para o cálculo de fatorial de um número
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):
            f *= c
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        return f


# Programa Principal
print('-' * 30)
print(fatorial(5, True))
help(fatorial)
