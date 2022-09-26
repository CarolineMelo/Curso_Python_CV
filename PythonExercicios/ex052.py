# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
number = int(input('Digite um número inteiro: '))
for c in range(1, number+1):
    if number % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
