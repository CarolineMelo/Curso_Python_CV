# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra 💎','Papel 🧻', 'Tesoura ✂️')
computador = randint(0, 2)

print('''Suas opções: 
[0] PEDRA 💎
[1] PAPEL 🧻
[2] TESOURA ✂️''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PÔ!!!')
sleep(1)
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)


if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('VOCÊ GANHOU!🎉')
    elif jogador == 2:
        print('Computador GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('VOCÊ GANHOU🎉')
    else:
        print('JOGADA INVÁLIDA!')

elif computador ==2:
    if jogador == 0:
        print('VOCÊ GANHOU!🎉')
    elif jogador == 1:
        print('computador GANHOU!')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVÁLIDA!')
