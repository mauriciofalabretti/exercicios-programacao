from math import fsum

#Função para validar resposta
def valida_resposta(mensagem: str) -> str:
    while True:
        try:
            resposta = str(input(mensagem)).strip().upper()
            if resposta != 'N' and resposta != 'S':
                raise ValueError('Resposta inválida!')
            return resposta
        except ValueError as e:
            if 'Resposta inválida' in str(e):
                print(f'\033[0;91mDigite S para Sim ou N para Não!\033[m {e}')


#Função para validar a nota
def valida_nota(mensagem: str) -> float:
    while True:
        try:
            nota = float(input(mensagem))
            if nota < 0 or nota > 10: #Regra de negócio
                raise ValueError('Nota inválida!')
            return nota
        except ValueError as e:
            if 'Nota inválida!' in str(e):
                print(f'\033[0;91mNota deve estar entre 0 e 10!\033[m Tente novamente! {e}')
            else:
                print(f'\033[0;91mValor inválido! Digite uma nota válida!\033[m {e}')


#Declara a lista de alunos e inicia o loop para entrada de dados
alunos = []
while True: #alunos é estruturado em listas compostas: alunos[nome, [n1, n2], [média]]
    alunos.append([str(input('Nome: ')),[valida_nota('Nota 1: '), valida_nota('Nota 2: ')], []])
    for i in range(len(alunos)): #loop para cálculo da média
        alunos[i][2] = fsum(alunos[i][1]) / 2
    continuar = valida_resposta('Deseja continuar? [S/N] ')
    if continuar == 'N':
        break

#Apresentação dos resultados
print('-' * 50)
print('Nº  NOME           MÉDIA')
print(f'=' * 30)
for i, aluno in enumerate(alunos):
    print(f'{i:<3} {aluno[0]:<10} {aluno[2]:>9.1f}')
print(f'-' * 30)

while True:
    notas_ind = int(input('Mostrar as notas de qual aluno(a)? (999 interrompe) '))
    if notas_ind == 999:
        print('Finalizando...')
        break
    if notas_ind <= len(alunos) - 1:
        print(f'As notas de {alunos[notas_ind][0]} são: {alunos[notas_ind][1]}')
