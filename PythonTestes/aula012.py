nome = str(input('Qual e o seu nome? '))
if nome == 'Ana':
    print('Que nome bonit0!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paloma':
    print('{}, seu nome é bem popular no Brasil' .format(nome))
elif nome in 'Carol Cléo Bete Bia Juliana':
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}' .format(nome))