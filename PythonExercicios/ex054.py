# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year

countMaior = 0
countMenor = 0
for c in range(1,8):
    anoNascimento = int(input("Digite ano que a {}ª pessoa nasceu: ".format(c)))
    idade = ano - anoNascimento
    if idade >= 18:
        countMaior += 1
    else:
        countMenor += 1

print("Total de pessoas maiores de idade é {}".format(countMaior))
print("Total de pessoas menores de idade é {}".format(countMenor))
        

