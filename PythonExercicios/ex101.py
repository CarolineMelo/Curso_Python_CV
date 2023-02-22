'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date

def voto(nasc):
    hoje = date.today()
    idade = hoje.year - nasc
    print(idade)
    if idade>=18:
        v = 'Obrigatório' 
    else:
        v= 'Opcional'
    print(f'Com {idade}anos de idade o voto é {v}')    

nascimento = int(input('Em que ano você nasceu?'))
voto(nascimento)


#Classe date dentro da função para econmizar memória.)
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
# print(voto(1980))
nascimento = int(input('Em que ano você nasceu?'))
print(voto(nascimento))    
