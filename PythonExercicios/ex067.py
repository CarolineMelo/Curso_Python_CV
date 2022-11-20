# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    c = 0
    print('_'*40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('_'*40)
   
    if n < 0:
        break
   
    while c < 10:
        c += 1
        print(f'{n} X {c} = {n*c}')
    
print('Fim')
