'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
pessoas = {}
pessoas['nome']= str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoas['idade'] = datetime.now().year - nascimento
pessoas['ctps'] = float(input('Carteira de Trabalho (0 não tem): '))

if pessoas['ctps'] != 0:
    pessoas['contratacao']= int(input('Ano de contratação: '))
    pessoas['salário'] = float(input('Salário: R$'))
    pessoas['aposentadoria'] = ((pessoas['contratacao'] + 35) - datetime.now().year) + pessoas['idade']

print('-='*40)
for k, v in pessoas.items():
    print(f' - {k} tem o valor {v}')
  
