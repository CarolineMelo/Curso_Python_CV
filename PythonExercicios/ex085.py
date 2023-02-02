'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

valores = list()
for c in range(0, 7):
    valores.append(int(input(f'Digite o {c+1}º valor:')))
print('-='*20)
# print(f'Os valores digitados foram: {(valores)}')

print(f'Os valores pares digitados foram:', end=' ')
for v in valores:
    if v % 2 == 0:
        print(f'[{v}] ', end='')
print()

print(f'Os valores ímpares digitados foram: ', end=' ')
for v in valores:
    if v % 2 != 0:
        print(f'[{v}]' , end=' ')
print()
'''RESOLUÇÃO DO PROFESSOR'''
núm = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*40)
núm[0].sort
núm[1].sort
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
