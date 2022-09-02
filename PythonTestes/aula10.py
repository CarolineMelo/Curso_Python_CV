
nome = input('Digite seu nome: ')
if nome == 'Carol':
    print('{}, seu nome é lindo'.format(nome))
else:
    print("Seu nome é tão blábláblá...")
print('Bom dia, {}.'.format(nome))

print(20*'-')
n1 = int(input('Digite a primeira nota: ')) 
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2)/2
# print('Aprovado' if m>=6 else 'Reprovado')
if m >=6:
    print('Aprovado')
else:
    print('Reprovado') 
print('A sua média foi {}'.format(m))

