'''print('='*20)
nome = input('Qual é o seu nome? ')
print('Prazer em conhecer {:=^20}! '.format(nome))
print('Prazer em conhecer {:=<20}! '.format(nome))
print('Prazer em conhecer {:=<20}! '.format(nome))'''

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo valor: '))
soma = number1 + number2
mult = number1 * number2
div = number1 / number2
div_inteira = number1 // number2
exp = number1 ** number2
print(' A soma é {},\n O produto é {},\n A divisão é {:.2f}' .format(soma,mult,div), end='   ')
print('Divisão inteira {} e potência {}'.format(div_inteira,exp))