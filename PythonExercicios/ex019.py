# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome escolhido.
from random import choice
aluno1 = input('Nome do rimeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido =choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))