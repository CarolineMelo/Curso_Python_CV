# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura =float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
litro_tinta = area/2
print('Sua parede tem a dimensão de {:.2f} X {:.2f} e sua área é de {:.1f}m²'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litro_tinta))
