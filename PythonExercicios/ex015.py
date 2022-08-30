#Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,15 por Km rodado.
km = float(input('Qual a quantidade de km percorrido?'))
dias = int(input('Quantos dias alugados?'))
custo =(dias *60) + (km * 0.15)
print('O preço a pagar é {:.2f}'.format(custo))