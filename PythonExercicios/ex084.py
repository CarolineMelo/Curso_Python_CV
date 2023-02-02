'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final,mostre: 
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.'''

pessoa = list()
galera = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1] 
        else:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()

    resp=' '
    while resp not in 'SN':
        resp= str(input('Quer continuar [S/N]: ')).upper().split()[0]
    if resp in 'N':
        break


print(f'Ao todo, você cadastrou {len(galera)} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} ' , end='')
print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]} ' , end='')