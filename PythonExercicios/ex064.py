# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = 0
number= 0
total = 0
while True:
    
    number = int(input('Digite um valor inteiro [999 para parar]: '))
    if number == 999:
        break
    contador +=1
    total += number
print('Você digitou {} números e a soma entre eles foi {}'.format(contador,total))