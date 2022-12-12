'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
maiorIdade = contH = contM = 0

while True:
    print('   Sistema de Cadastro de Pessoas')
    print('_'*40)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F]: ")).upper().strip()[0]

    if idade >= 18:
        maiorIdade += 1

    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

   


print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Total de homens cadastrados: {contH}')
print(f'Total de  {contM} mulheres com menos de 20anos')
