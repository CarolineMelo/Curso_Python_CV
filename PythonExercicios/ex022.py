'''Analisador de Textos
  Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo:'))

print('Seu nome em maiúsculo é ' + nome.upper())
print('Seu nome em minúsculo é ' + nome.lower())
print('Seu nome tem ao todo {} letras'.format(
    len(nome.strip()) - nome.count(' ')))
print('Seu primeiro nome é {} letras'.format(nome.find(' ')))
# print('Seu primeiro nome é '+ nome.find(''))

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(
    separa[0], len(separa[0])))
