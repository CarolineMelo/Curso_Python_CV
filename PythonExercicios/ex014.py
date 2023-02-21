# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
temp_c = float(input('Imforme a temperatura em °C:'))
temp_f = ((9 * temp_c)/5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(temp_c, temp_f))
