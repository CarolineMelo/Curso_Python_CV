# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumerics())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculo? ', x.isupper())
print('Está em minúscula? ', x.islower())
print('Está capitalizada? ', x.istitle())
