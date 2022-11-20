# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


number = cont = maior = menor = soma = 0
resp = 'S'
while resp in 'S':
    number = int(input("Digite um número:"))
    cont +=1
    soma +=number
    if cont == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        else:
            menor = number
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma/cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))