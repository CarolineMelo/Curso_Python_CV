# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano você quer analisar?'))
if ano == 0: 
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

# Para saber quando será Ano Bissexto devemos seguir o seguinte princípio:
# todos os anos múltiplos de 4 que também não são múltiplos de 100,
# com exceção dos múltiplos de 400, deverão ser anos bissextos.
