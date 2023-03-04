# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
from lib.interface import *
from time import sleep
while True:
    resp = menu(['Pessoas Cadastradas','Cadastrar nova Pessoa','Listar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        cabeçalho('Opção 1')
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

