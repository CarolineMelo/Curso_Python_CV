# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    number = int(input('Digite o {}º valor: '.format(c)))
    
    if number % 2 == 0:
        soma += number
        cont +=1
print('Você digitou {} números PARES e a soma entre eles é {}.'.format(cont, soma))