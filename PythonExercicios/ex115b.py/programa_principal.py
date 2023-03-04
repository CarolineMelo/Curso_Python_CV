# Exercício Python 115b: Vamos criar um menu em Python, usando modularização.
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'carolinemelo.txt'
# if arquivoExiste(arq):
#     print('Arquivo encontrado com sucesso!')
# else:
#     print('Arquivo não encontrado!')
#     criarArquivo(arq)

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Pessoas Cadastradas','Cadastrar nova Pessoa','Listar Pessoas', 'Sair do Sistema'])
    if resp == 1:
       #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

