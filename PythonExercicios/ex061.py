# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA')
print('-='* 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 1
while contador <=10:
    print(' {} -> '.format(termo), end='')
    termo += razao
    contador +=1
print('Fim')
