'''Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''
from utilidades import moeda

#Programa principal
valor = float(input("Digite o valor: R$"))
# moeda.resumo(valor)

moeda.resumo(valor,20,12)