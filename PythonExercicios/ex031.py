# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# parta viagens mais longas.

#(if simplificado)preco = distancia * 0.50 if distancia <= 200 else distancia *0.45

distancia = float(input('Qual é a distância da sua viagem? '))
if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.50 * distancia
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
print('E o preço da passagem será de R${:.2f}'.format(preco))
