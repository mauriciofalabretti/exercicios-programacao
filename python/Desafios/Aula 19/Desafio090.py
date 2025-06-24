#Declaração, estruturação e preenchimento do dicionário
aluno = {'nome': None, 'media': None, 'situacao': None}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

if aluno['media'] >= 7: #Condicional para definir a situação do aluno
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Em Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

#Apresentação dos valores
print('-' * 40)
for k, v in aluno.items():
    print(f'{k} é igual {v}')
