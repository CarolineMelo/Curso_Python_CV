# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120
'''Primeirea resolusão:
from math import factorial

number = int(input('Digite um número para calcular seu Fatorial:'))
f = factorial(number)
print('O fatorial de {} é {}'.format(number,f) )'''

'''Segunda resolusão:'''

number = int(input("Digite um número para calcular seu Fatorial: "))
contador = number
f = 1
print('Calculando {}! = '.format(number), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print( ' x ' if contador > 1 else '=', end='')
    f *= contador
    contador -=1
print(' {} '.format(f))
