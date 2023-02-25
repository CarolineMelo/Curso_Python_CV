'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input("Digite um número entre  0 e 20: "))
    if 0 <= number <= 20:
        break
    print('Tente novamente')

    print(f' Você digitou o número {cont[number]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
