#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))
centimetros = metros*100
milimetros = metros*1000
print('{} metros convertidos para centímetros é {:.0f}cm e em milímetros é {:.0f}mm'.format(metros,centimetros,milimetros))
