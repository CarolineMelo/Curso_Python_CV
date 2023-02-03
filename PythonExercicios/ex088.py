'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
# from random import randint
# lista = []
# jogos = []
# quantidade = int(input('Quantos jogos você deseja fazer: '))
# for c in range(0, quantidade):

#     for c in range(0, 6):


#         num = randint(1, 60) 
#         if num not in lista:
#             lista.append(num)
'''Aqui, o número gerado pelo randint é adicionado à lista lista somente se ele ainda não estiver presente na lista. Isso significa que se o número gerado já tiver sido adicionado anteriormente, ele não será incluído novamente e a lista lista poderá ter menos de 6 elementos.

Para garantir que sempre haja 6 números na lista lista, basta remover a condição if num not in lista: e adicionar o número gerado sempre que o loop for executado.'''

#     jogos.append(lista[:])
#     lista.clear()
    

# print('-'*40)
# print(f'{"MEGA SENA":^40}')
# print('-'*40)
# print('-='*5, f'Sorteando {quantidade} Jogos ','-='*5)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')

'''Como eu corrigi esse erro: '''
from random import randint
lista = []
jogos = []
quantidade = int(input('Quantos jogos você deseja fazer: '))
for c in range(0, quantidade):

    while len(lista) < 6:
        num = randint(1, 60)
        lista.append(num)

    jogos.append(lista[:])
    lista.clear()
    

print('-'*40)
print(f'{"MEGA SENA":^40}')
print('-'*40)
print('-='*5, f'Sorteando {quantidade} Jogos ','-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

