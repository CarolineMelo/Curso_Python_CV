# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = -1
number= 0
total = 0
while number != 999:
    total += number
    contador +=1
    number = int(input('Digite um valor inteiro [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}'.format(contador,total))