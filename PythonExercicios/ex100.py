'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando números da lista: ',end='')
    for c in range(0,5):
        num= randint(0,10)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('✅')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Soma dos números pares: {soma}')

    
números = list()
sorteia(números)
somaPar(números)