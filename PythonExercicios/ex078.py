number = []
for cont in range(0,5):
    number.append(int(input(f'Digite um valor para a Posição {cont +1}:')))
print('-=-'*20)

print(f'Você digitou os valores {number}')
max=max(number)
min=min(number)
print(f'O maior valor digitado foi {max} na posição {number.index(max)+1}')
print(f'O menor valor digitado foi {min} na posição {number.index(min)+1}')
