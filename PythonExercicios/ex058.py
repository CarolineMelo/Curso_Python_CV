# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
numComputador = randint(0,10)
print(numComputador)

print("Será que você consegue adivinhar qual foi?")
cont = 0
acertou = False
while not acertou:
   numUsuario = int(input('Qual é o seu palpite?'))
   cont = cont + 1
   if numComputador == numUsuario:
    acertou = True
    
   else:
    if numComputador > numUsuario:
     print('Mais.. Tente mais uma vez.')
    else:
     print('Menos.. Tente mais uma vez.') 
print('Acertou. O número sorteado foi {}!'.format(numComputador)) 
print('Você acertou em {} tentativas.'.format(cont))
