import statistics

# Função para analisar notas e verificar situação de aluno
def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    info_aluno = {
        'total': len(nota),
        'maior': max(nota),
        'menor': min(nota),
        'media': statistics.mean(nota)
    }

    if sit == True:
        if info_aluno['media'] >= 7:
            info_aluno['situacao'] = 'BOA'
        elif info_aluno['media'] >= 5 and info_aluno['media'] < 7:
            info_aluno['situacao'] = 'RAZOÁVEL'
        else:
            info_aluno['situacao'] = 'RUIM'

    return info_aluno


# Programa Principal
resp = notas(10, 7.5, 6.5, 7, 9.5, sit=True)
print(resp)
help(notas)
