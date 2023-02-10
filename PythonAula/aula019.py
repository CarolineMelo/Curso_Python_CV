'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

Variáveis compostas:
-Tuplas ()
-Listas []
-Dicionários {}

RECORDANDO: Em Lista 
dados =list()
dados.append('Pedro')
dados.append(25)


Agora em DICIONÁRIO: -> indices literais
em dicionário o append não funciona
'''

# dados = dict()  ou
# dados = {}
# dados = {'nome':'Pedro','idade':25}
# print(dados['nome'])
# print(dados['idade'])
# dados['sexo']='M'
# del dados['idade']
# print(dados)


'''pessoas = {'nome': 'Gustavo','sexo':'M','idade':22}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(pessoas['nome'])
print(f' O {pessoas["nome"]} tem {pessoas["idade"]}anos.')
del pessoas['sexo']
pessoas['peso']=98.5 #adicionei sem o append
for k,v in pessoas.items():
    print(f'{k} = {v}')'''


'''filme = { 'titulo': 'Star Wars','ano':1997,'diretor':'GeorgeLucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')'''


'''No dicionário eu não consigo fazer o fatiamento como na lista. Então para copiar ao invez de [:] eu posso usar o método interno copy()'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()