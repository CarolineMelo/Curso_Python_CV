#Crie um programa que leia um número real qualquer 
# pelo teclado e mostre na tela a sua porção inteira
'''from math import floor
number = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(number,floor(number)))


n = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}.'.format(n,int(n)))'''

from math import trunc
n = float(input('Digite um valor:'))
print('O número {} tem a parte inteira {}.'.format(n,trunc(n)))