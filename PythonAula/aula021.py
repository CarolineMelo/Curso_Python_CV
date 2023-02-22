'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''

#  -> Interactive help

'''help(print)

Interactive help é um recurso do Python que permite que você obtenha informações sobre como usar funções, métodos, classes e outros recursos da linguagem.'''

#  -> docstrings

def calcular_media(lista):
    """
    Calcula a média dos números em uma lista.
    :param lista: uma lista de números
    :return: a média dos números na lista
    """
    return sum(lista) / len(lista)

# -> Argumentos opcionais

def adicionar(a, b=0, c=0):
	return a + b + c

adicionar(2) # saída: 2
adicionar(2, 3) # saída: 5
adicionar(2, 3, 4) # saída: 9

# -> Escopo de variáveis

x = 5

def funcao():
    global x
    x = 10
    print(x)

funcao() # saída: 10
print(x) # saída: 10


# -> Retorno de resultados

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')