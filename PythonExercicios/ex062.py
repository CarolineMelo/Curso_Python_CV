# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerenciador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 1
total = 0
qtd = 10
while qtd != 0:
    total = total + qtd
    while c <= total:
        print(' {} '.format(termo), end='')
        termo += razao
        c +=1
    print('PAUSA')
    qtd = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
