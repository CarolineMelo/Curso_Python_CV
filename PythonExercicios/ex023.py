'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

'''number = int(input('Digite um número: '))
n = str(number)
print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

n = int(input('Digite um número: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(unidade))
print('Centena: {}'.format(dezena))
print('Dezena: {}'.format(centena))
print('Milhar: {}'.format(milhar))