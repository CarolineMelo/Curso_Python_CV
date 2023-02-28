import moeda

#Programa principal
valor = float(input("Digite o valor: R$"))
print(f'A metade de R${valor} é {moeda.metade(valor)}')
print(f'O dobro de R${valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos  R${moeda.aumentar(valor,10)}')
print(f'Diminuindo 20%, temos  R${moeda.diminuir(valor,20)}')
