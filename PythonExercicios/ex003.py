# Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
s = number1 + number2
print('A soma de {} mais {} é igual a {}!'.format(number1,number2,s))