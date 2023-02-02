# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

''' Variáveis compostas (Lista) parte 2

dados = list() é uma lista e por isso é mutavel
uma tpla não é mutavel

'''
# Primeiro exemplo:
'''dados= list()
dados.append('Carol')
dados.append(33)
print(dados[1])
pessoas= list()
pessoas.append(dados[:])
print(pessoas)

pessoas=[['Carol',33],['Maria',22],['Carlos',40]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[1][1])
print(pessoas[2][0])'''

# Segundo exemplo:
'''teste = list()
teste.append('Caroline')
teste.append(25)
galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 33
galera.append(teste[:])
print(galera)'''

# Terceiro exemplo:
'''galera = [['Luiz',7],['Ana',10],['Carlos',40],['Miguel',12]]
print(galera[0][0])

for p in galera:
    print(p[0])
    # ou posso fazer o print formatado
    print(f'{p[0]} tem {p[1]} anos idade.')'''

# Quarto exemplo:

galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  
    dado.clear()
print(galera)

for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')

