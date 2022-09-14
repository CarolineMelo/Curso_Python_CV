# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

year_birth = int(input('Digite o seu ano de nascimento: '))
current_year = date.today().year
age = current_year - year_birth

if age < 18:

    s = 18 - age
    year = current_year + s

    print('Quem nasceu em {} tem {} anos. Faltam {} anos para o alistamento.'.format(year_birth, age, s))
    print('Seu alistamento será {}'.format(year))

elif age > 18:

    s = age - 18
    year = current_year - s

    print('Você tem {} anos, já passou {}anos do seu período de alistamento!'.format(age, s))
    print('Seu alistamento foi em {}.'.format(year))

else:
    print('Você tem {} anos, esse é o período exato para se alistar!'.format(age))
