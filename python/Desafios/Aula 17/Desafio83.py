expressao = str(input('Digite uma expressão matemática com uso de parênteses: ')).strip()
pilha = []

for i in expressao:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break #No momento em que adicionar um ")" na pilha com ela vazia, está errado

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não está válida!')
