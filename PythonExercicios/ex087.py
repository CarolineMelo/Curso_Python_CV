# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = maior = somacoluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*40)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if matriz[l][c] %2 == 0:
            par += matriz[l][c]

    print()
print(f'A soma dos valores pares é {par}')

for l in range(0,3):
    somacoluna += matriz[l][2]
print(f'A soma dos elementos da terceira coluna é {somacoluna}')

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz [1][c] > maior:
        maior= matriz[1][c]

print(f'O maior valor da segunda linha é {maior}')
