# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
number = int(input('Digite um número inteiro: '))
print('[1] converter para binário')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
option = int(input('Escolha uma das base para conversão: '))


if option == 1:
    print('O número {} convertido para binário é {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('O número {} convertido para octal é {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('O número {} convertido para hexadecimal é {}'.format(number, hex(number)[2:]))
else : print('opção inválida')