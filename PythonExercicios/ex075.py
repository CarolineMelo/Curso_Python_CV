'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
number=(int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))

print(f'Você digitou os valores {number}')
print(f'O valor 9 apareceu {number.count(9)} vezes')
if 3 in number:
    print(f'O número 3 está na {number.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in number:
 if n % 2 == 0:
    print(f'Os valores pares digitados foram {n}', end=' ')