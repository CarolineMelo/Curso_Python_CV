'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''


def aumentar(valor, taxa):
    resultado =  valor + (valor * taxa/100)
    return resultado

def diminuir(valor, taxa):
    resultado = valor - (valor * taxa/100)
    return resultado



def dobro(valor):
    resultado =  valor * 2
    return resultado


def metade(valor):
    resultado = valor / 2
    return resultado


