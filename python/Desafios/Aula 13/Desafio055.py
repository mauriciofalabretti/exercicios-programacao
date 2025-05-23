#Função para validar a entrada float
def valida_entrada(mensagem: str) -> float:
    while True:
        try:
            entrada = float(input(mensagem))
            if entrada <= 0: #Regra de negócio
                raise ValueError('Valor inválido!')
            return entrada
        except ValueError as e:
            if 'Valor inválido!' in str(e):
                print(f'\033[0;91mValor deve ser superior à zero!\033[m {e}')
            else:
                print(f'\033[0;91mDado inserido é de tipo inválido!\033[m {e}')
        except Exception as e:
            print(f'\033[0;91mErro inesperado! \033[m {e}')

#Entrada de dados dentro do loop
maior_peso = 0 #Inicializa a variável do maior peso
menor_peso = None #Inicializa a variável de menor peso

for i in range(5):
    peso = valida_entrada(f'Digite o {i + 1}º peso: ')
    if peso > maior_peso:
        maior_peso = peso
    if menor_peso is None or peso < menor_peso:
        menor_peso = peso

#Saída mostrando o menor e o maior peso registrados
print(f'\033[0;95mO menor peso foi {menor_peso:.1f} Kg\033[m')
print(f'\033[0;96mO maior peso foi {maior_peso:.1f} Kg\033[m')
