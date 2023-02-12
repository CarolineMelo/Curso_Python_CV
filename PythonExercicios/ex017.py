'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''
#import math
from math import hypot
cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))

#h = (cat_oposto **2 + cat_adjacente**2) ** (1/2)
#h = sqrt(pow(cat_oposto,2) + pow(cat_adjacente,2))
h = hypot(cat_oposto,cat_adjacente)
print('A hipotenusa vai medir {:.2f}'.format(h))