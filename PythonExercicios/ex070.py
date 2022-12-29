'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = totalMil = menor = 0
cont = 0
produto=''
while True:
    nome= str(input('Nome do Produto: '))
    preco= int(input('Preço: '))
    cont +=1
    total += preco
    if preco > 1000:
        totalMil +=1

    if cont == 1 or preco < menor:
       menor = preco
       produto = nome
    
    resp= ' '
    
    while resp not in 'SN':
        resp= str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if resp == 'N':
        break
   

print('-----FIM DO PROGRAMA -----')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totalMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto} que custa R$ {menor:.2f}')