salary = float(input('Qual é o salário do Funcioário? R$'))
salary_readjusted = salary + (salary*15/100)
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salary,salary_readjusted))