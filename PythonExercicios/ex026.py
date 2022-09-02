frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))


# rfind é procure a partir do lado direito
#Exercício 26 – Primeira e última ocorrência de uma string