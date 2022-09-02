'''Exercício Python 28: 
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
num = randint(1, 5)
print('-=-'*20)
print('Vou pensar em um número entre zero e cinco. Tente advinhar...')
print('-=-'*20)

number = (int(input('Qual foi o número escolhido pelo computador: ')))
print('Processando...')
sleep(2)
if number == num:
    print('Parabéns! Você acertou! O numero sortiado foi {}!'.format(num))
else:
    print('Infelizmente você errou. O número sorteado foi {}!'.format(num))
print('Fim')
