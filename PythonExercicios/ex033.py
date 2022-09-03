# Exercício Python 33:
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Primeiro valor: '))
n3 = int(input('Primeiro valor: '))

if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi {}'.format(n1))
elif n2 > n3:
    print('O maior valor digitado foi {}'.format(n2))
else:
    print('O maior valor digitado foi {}'.format(n3))

# Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))
