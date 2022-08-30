#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.
number = int(input('Digite um número: '))
print('O número digitado é {}.\nO seu dobro é {}.\nO seu triplo é {}.\nE sua raiz quadrada é {:.2f}' .format(number,number*2,number*3,number **(1/2)))

#pow(number,(1/2))