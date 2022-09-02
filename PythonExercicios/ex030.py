#Exercício Python 30: 
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
number = int(input('Digite um número qualquer: '))
if number % 2 != 0:
    print('O número {} é ímpar'.format(number))
else:
    print('O número {} é par'.format(number))
