#Loop para validar a entrada do usuário
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo: [M/F] ')).upper().strip()[0] #Fatia a string pegando só a primeira posição
    if sexo != 'M' and sexo != 'F':
        print(f'\033[0;31mDado inserido é inválido!\033[m Tente novamente!')

if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso!')

print('Tudo certo! Pode prosseguir!')
