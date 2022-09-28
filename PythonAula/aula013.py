#Laços de Repetição OU iteração

# for c in range(0,4):
#     print('oi')
# print('Fim')

from tkinter import N

for c in range(4,0,-1): #diminuindo 
    print(c)
print('Fim')
for c in range(0,7,2): #diminuindo 
    print(c)
print('Fim')

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i,f+1,p): 
#     print(c)
# print('Fim')

s = 0
for c in range(0,2):
    n= int(input('Digite um valor: '))
    s += n
print ('A somatoria de todos os números é {}'.format(s))
