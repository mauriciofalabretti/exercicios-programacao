#Função para validar entrada de inteiros
def valida_inteiro(mensagem: str) -> int:
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError as e:
            print(f'\033[0;91mValor deve ser um número inteiro!\033[m Tente novamente! {e}')


#Programa principal
lista = list()
aux_pos = None

for i in range(5): #Loop para entrada de dados
    valor = valida_inteiro('Digite um valor: ')
    if i == 0: #Condição para inserção do primeiro valor
        lista.insert(0, valor)
        print('Adicionado ao final da lista...')
    else: #Começa na segunda iteração
        for j in range(len(lista)): #Loop para varredura da lista de acordo com o tamanho
            if valor > lista[j]: #Se o valor digitado for maior que o da atual posição
                aux_pos = j + 1 #Salva a posição seguinte numa variável auxiliar
            elif valor < lista[j]: #Se o valor for menor que o da atual posição
                aux_pos = j #Guarda a primeira ocorrência na variável auxiliar
                break
        lista.insert(aux_pos, valor) #Ao final da varredura, insere o valor na posição certa
        if aux_pos == len(lista) - 1:
            print('Adicionado ao final da lista...')
        else:
            print(f'Adicionado na posição {aux_pos} da lista...')


#Apresentação dos resultados
print('-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
