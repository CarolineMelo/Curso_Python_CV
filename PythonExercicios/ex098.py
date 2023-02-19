'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
'''

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}: ', end='')
    print()
    sleep(2)
    
    if p < 0:
        p =-p
    if i > f:
        f -= 1
        p= -p
    else: f +=1
    for c in range(i, f, p):
        print(f'{c} ', end='', flush=True)   
        sleep(1)
    print()
        



contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('início: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo)'''



#SOLUÇÃO DO PROFESSOR: 
from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('-='* 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i 
        while cont <= f:
            print(f'{cont} ', end='', flush=True) #flush=True é para resolvers o buffer /buffer de tela é uma matriz bidimensional de caracteres e dados de cor para saída em uma janela de console
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -=p
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)

