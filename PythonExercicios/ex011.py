largura =float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
litro_tinta = area/2
print('Sua parede tem a dimensão de {:.2f} X {:.2f} e sua área é de {:.1f}m2'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {} de tinta'.format(litro_tinta))