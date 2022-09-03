# Exercício Python 34: 
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
# o aumento é de 15%.
salary = float(input('Qual é o salário do funcionário?'))
if salary >1250:
    salary_readjusted = salary + (10/100 * salary)
else:
    salary_readjusted = salary + (15/100 * salary)
print('Quem ganha {:.2f} passa a ganhar R$ R${:.2f} agora'.format(salary,salary_readjusted))