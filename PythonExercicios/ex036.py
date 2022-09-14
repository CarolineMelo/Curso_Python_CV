# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Valor da casa: R$'))
salary = float(input('Salário do comprador: R$'))
years_paying = int(input('Anos de financiamento: '))
monthly_installment = house_value / (years_paying * 12)
percentage = (salary * 30/100)
print('Para pagar uma casa de  R$ {:.2f} em {}anos '.format(house_value,years_paying),end='')
print('a prestação será de R${:.2f}'.format(monthly_installment))
if monthly_installment <= percentage:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
