palavras = ('singapura', 'palmeira', 'violeta', 'vinagre', 'bombom', 'chiclete',
            'fermento', 'casaco', 'borrifador', 'tesouro', 'estiagem', 'sorvete')

for i in range(0, len(palavras)): #Para cada item dentro da tupla palavras
    print(f'\nNa palavra {str(palavras[i]).upper()} temos', end=' ') #Introduz a palavra de acordo com o índice atual
    for letra in palavras[i]: #Para letra/item dentro da palavra atual
        if letra in 'aeiou': #Verifico se a letra faz parte da tupla vogais
            print(letra, end=' ') #Se faz, eu imprimo a letra
