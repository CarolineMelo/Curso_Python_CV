''' Variáveis compostas (Listas) Parte 1 - Fase 17

tuplas = ()  Tuplas são imutáveis
lista = []   Listas podem ser modificadas
'''

frutas = [ 'Banana', 'Morango', 'Abacaxi', 'Caju']
print(frutas)
frutas[3] = 'Laranja'
print(frutas)

'''Resultado : O item da lista pode ser alterado!
['Banana', 'Morango', 'Abacaxi', 'Caju']
['Banana', 'Morango', 'Abacaxi', 'Laranja']

Para adicionar elemento na lista podemos usar o método append/ O append adiciona no FINAL DA LISTA'''
frutas.append('MELÃO')
print(frutas)

'''Resultado: O tamanho da lista pode ser alterado!
['Banana', 'Morango', 'Abacaxi', 'Laranja', 'MELÃO']

Para adicionar UM elemento na lista EMPURRANDO E OCUPANDO O index do elemento anterior podemos usar o método insert
'''

frutas.insert(0,'Amora')
print(frutas)

'''Resultado: 
['Banana', 'Morango', 'Abacaxi', 'Laranja', 'MELÃO']
['Amora', 'Banana', 'Morango', 'Abacaxi', 'Laranja', 'MELÃO']


Para apagar elemento 
del frutas[3] - comando básico
frutas.pop(3) -> Normalmente o pop é usado para eliminar o último elemento / sem passar o número do índice (frutas.pop()) ele eliminará o último indice
frutas.remove('MELÃO') -> Elimina o elemento e repocisiona a contagem dos índeces
'''
frutas.remove('Amora')
frutas.pop()
frutas.pop(1)
print(frutas)

if 'Leite' in frutas:
    frutas.remove('Leite')

valores = list(range(4,11))
valores = [8,2,5,4,9,3,0]
# valores.sort() Coloca os valores em ordem crescente
# valores.sort(reverse=True) Coloca em ordem decrescente
# len(valores)

num = [2,5,9,1]
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
        num.remove(4)
else:
    print(num)
    print(f'Essa lista tem {len(num)} elementos.')






'''val = []
val.append(5)
val.append(9)
val.append(4)'''
val = []
for cont in range(0,5):
    val.append(int(input('Digite um valor: ')))
for c, v in enumerate(val):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final da lista.')





'''Exemplo: Para copiar b= a[:] (Fatiamento) / Para interligar b = a (a recebe b faz com que as duas listas tenham uma ligação e com isso ao alterar uma delas estarei modificando as duas na vdd'''

a = [2,3,4,7]
# b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')