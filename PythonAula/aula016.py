''' Variável simples: Guarda apenas um valor
 Variável composta: Pode guardar vários valores -> Três tipos: tuplas(), listas[] e dicionários{}.
 
 Fatiamento: [1:] -> vai do primeiro até o último
 Fatiamento: [-1] -> último

len(lanhe) -> vai mostrar a quantidade total

"AS TUPLAS SÃO IMUTÁVEIS"

 
 '''
frutas = ('Morango', 'melão', 'banana')
# print(frutas[-2])
# print(len(frutas))

# Acessar elemento da tupla de duas formas diferentes: 
for cont in range(0,len(frutas)):
    print(f'Eu gosto de {(frutas[cont])} na posição {cont}')

#Ou -> Mesmo resultado

for comida in frutas:
    print(f'Vou comer {comida}')

#Exemplo com enumerate

for pos, comida in enumerate(frutas):
    print(f'Eu vou comer {comida} na posição {pos}')

#Método sorted -> Coloca em ordem
lanche = ('Tapioca','Amendoim', 'Panqueca', 'Biscoito')
print(sorted(lanche))
print(lanche)

##############################################################

a= (2,3,4)
b= (5,8,1,2)
c = b + a
#NÃO É POSSÍVEL DELETAR/ALTERAR UM ITEM DA TUPLA, MAS É POSSÍVEL DELETAR A TUPLA INTEIRA -> 
# del(a)
print(a)
print(c)
print(c.count(2))

print(c.index(8))


