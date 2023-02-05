'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
aluno = []
media = 0
while True:

    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    lista.append(aluno[:])
    aluno.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break
print(F'Nº   NOME   MÉDIA ')
for i, a in enumerate(lista):
    media = (a[1]+a[2]) / 2
    print(f'{i+1:^6} {a[0]:^6} {media:^6}')

opcao = int(input('Mostrar notas de qual aluno?  (999 interrompe):'))
if opcao != 999:
    if i+1 == opcao:
        print(f'Notas de {a[0]} são {a[1]} e {a[2]}')
else:
    print('FIM DO PROGRAMA!')
    
if opcao <= len(lista):
    print(
        f'Notas de {lista[opcao-1][0]} são {lista[opcao-1][1]} e {lista[opcao-1][2]}')
else:
    print('Opção inválida! Tente novamente.')
