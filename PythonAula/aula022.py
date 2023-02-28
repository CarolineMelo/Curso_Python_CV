'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.'''

'''Modularização
Surgiu no início da década de 60
Sistemas ficando cada vez maiores
Foco: dividir um programa grande
Foco: aumentar a legibilidade
Foco: facilitar a manutenção'''

def fatorial(n):
    f=1
    for c in range(1, n+1):
        f*=c
        return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
    
num = int(input("Digite um valor: "))
fat= fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')

'''
VANTAGENS

Organização do código
Facilidade na manutenção
Ocultação de código detalhado
Reutilização em outros projetos


PACOTES (em outras linguagem chamamos de biblioteca / No python é PACOTE!)
'''