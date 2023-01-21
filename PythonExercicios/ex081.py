lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp =' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break

print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
