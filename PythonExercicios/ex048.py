# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma entre os {} valores solicitados é {}'.format(cont,s))