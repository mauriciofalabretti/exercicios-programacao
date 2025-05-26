produtos = ('Jaqueta', 159.00, 'Bota', 129.90, 'Calça', 89.90, 'Camisa', 79.90, 'Moletom', 99.00,
            'Luvas', 29.90, 'Meias', 9.90, 'Cinto', 30.00, 'Gorro', 25.00, 'Camiseta', 49.90)

print('-' * 50)
print(f'{f'LISTAGEM DE PREÇOS':^50}')
print('-' * 50)

#Loop varre a tupla verificando os itens do tipo string e os do tipo float
for i in produtos:
    if type(i) == str:
        print(f'{i:.<40}R$', end=' ') #Se for uma string, é o nome do produto, então aguarda o preço na mesma linha
    else:
        print(f'{i:.2f}') #Se não for uma string, é o valor do produto, e ele é impresso na mesma linha

print('-' * 50)