#Verificando todos os números ímpares múltiplos de 3 no intervalo de 1 a 500 e calculando sua soma
soma = 0 #Inicializa a variável acumuladora
cont = 0 #Inicializa a variável contadora
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'A soma entre os ímpares múltiplos de três no intervalo de 1 a 500 é \033[0;92m{soma}\033[m.\n'
      f'Foram registrados \033[0;92m{cont}\033[m números atendendo aos requisitos.')
