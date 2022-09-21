# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS CAROL '))
price = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros''')

option = int(input('Escolha a forma de pagamento: '))
if option == 1:
    total = price-(price * 10/100)
   
elif option == 2:
    total = price-(price * 5/100)
    
elif option == 3:
    total = price
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    
elif option == 4:
    total = price + (price * 20/100)
    total_parcelas= int(input('Quantas parcelas: '))
    parcela = total/total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas,parcela))
print('O valor a ser pago é de R${:.2f}, vai custar {:.2f} no final'.format(price,total))
