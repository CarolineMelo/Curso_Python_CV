# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from mailbox import NotEmptyError

somaIdade = 0
countIdade = 0
countMulher = 0
maisVelho = 0
nomemaisVelho = ''
for pessoa in range(1,5):
   
    print("-=-=-=-= {}ª Pessoa -=-=-=-=".format(pessoa))
    nome = str(input("Digite o nome: ")).strip().upper()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()
    
    somaIdade +=idade
    countIdade += 1
    if sexo == "M":
        if pessoa == 1:
            maisVelho = idade
        else:
            if idade > maisVelho:
                maisVelho = idade
                nomemaisVelho = nome
    else:
        if idade < 20:
            countMulher +=1    



media = somaIdade/countIdade
print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maisVelho,nomemaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(countMulher))