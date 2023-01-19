valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores {valores}')