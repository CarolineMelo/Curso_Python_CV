'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0,5):
    valor = ((int(input('Digite um valor: '))))
    if c == 0:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    elif valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print(f'Os valores digitados em ordem foram {lista}')
