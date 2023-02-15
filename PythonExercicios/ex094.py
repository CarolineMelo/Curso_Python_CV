'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoa, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoa foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoa com idade acima da média'''

pessoas = []
mulheres = []
idades = []
contM = contH = 0

while True:
  pessoa = {}
  pessoa['nome'] = str(input('Nome: '))
  pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]

  while pessoa['sexo'] not in 'MF':
    print('Por favor, digite apenas M ou F.')
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]

  if pessoa['sexo'] == 'M':
    contM += 1
  else:
    contH += 1

  pessoa['idade'] = int(input('Idade: '))
  idades.append(pessoa['idade'])

  if pessoa['sexo'] == 'F':
    mulheres.append(pessoa.copy())

  pessoas.append(pessoa)

  resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
  while resp not in 'SN':
    print('ERRO! Responda apenas S ou N.')
    resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
  if resp in 'N':
    break


print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idades é {sum(idades)/len(idades)} anos')

print(f'C) Lista de mulheres:' , end=" ")
for mulher in mulheres:
  print(f'{mulher["nome"]}, {mulher["idade"]}anos')

print(f'D) Lista de pessoas com idade acima da média:')
for pessoa in pessoas:
  if pessoa['idade']> sum(idades)/len(idades):
    print(f'{pessoa["nome"]}, {pessoa["idade"]} anos')

print('<< ENCERRADO >>')








'''RESPOSTA DO PROFESSOR: ⬇ ''' 
'''galera = list()
pessoa = dict()
soma = média = 0
while True:
  pessoa.clear()
  pessoa['nome'] =  str(input('Nome: '))
  while True:
    pessoa['sexo']= str(input('Sexo: [M/F] ')).upper() [0]
    if pessoa ['sexo'] in 'MF':
      break
    print('ERRO! Por favor, digite apenas M ou F.')
  pessoa['idade'] = int (input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  while True:
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if resp == 'N':
    break
  print('-='* 30)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.') 
print(f'C) As mulheres cadastradas foram ', end ='')
for p in galera:
  if p['sexo'] in 'Ff':
    print(f'{p["nome"]} ',end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
  if p['idade'] >= média:
    print(' ', end='')
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<<ENCERRADO>>')'''