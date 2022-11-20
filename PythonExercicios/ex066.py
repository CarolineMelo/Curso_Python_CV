# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = 0
while True:
    number = int(input('Digite um valor inteiro: (999 para parar) '))
    if number == 999:
        break
    cont +=1
    soma +=number
print(f' A soma dos {cont} valores foi {soma}')