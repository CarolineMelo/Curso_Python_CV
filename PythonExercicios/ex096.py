'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def área(largura,comprimento):
    a = largura*comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {a}m²')


print('   Controle de Terrenos' )
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)