# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
number = []
for cont in range(0,5):
    number.append(int(input(f'Digite um valor para a Posição {cont +1}:')))
print('-=-'*20)

print(f'Você digitou os valores {number}')
max=max(number)
min=min(number)
print(f'O maior valor digitado foi {max} na {number.index(max)+1} posição ')
print(f'O menor valor digitado foi {min} na {number.index(min)+1} posição ')

