def maior(*núm):
    if len(núm) == 0:
        print('Nenhum valor foi informado.')
        return
    print('-='*40)
    print('Analisando os valores passados...')
    print(f'{núm} Foram informados {len(núm)} valores ao todo. ', end='')
    print(f'\nO maior valor informado foi {max(núm)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


#RESOLUÇÃO DO PROFESSOR
from time import sleep

def maior(*núm):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'{núm} Foram informados {cont} valores ao todo. ', end='')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()