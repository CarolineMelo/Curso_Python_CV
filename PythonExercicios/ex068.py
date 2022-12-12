# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
    print('-='*30)
    print('Vamos jogar par ou ímpar? ')
    print('-='*30)
    valor = int(input('Diga um valor: '))
    
    computador = randint(0,10)
    soma = valor + computador
    if soma%2 !=0:
        r = 'I'
        
    else:
        r = 'P'
       
    resp =' ' 
    while resp  not in 'PI': 
        resp = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        
    print(f'Você jogou {valor} e o Computador {computador}. Total de {soma} ', end='')
    print('Deu PAR' if soma %2 ==0 else ' Deu ÍMPAR')
    if resp == r:
        print('Você venceu!')
        vitoria +=1
    else:
        print('Perdeu!')
        break

print(f'Game over! Você venceu {vitoria} vezes.')
    