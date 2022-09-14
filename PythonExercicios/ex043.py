# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Peso (KG): '))
altura = float(input('Altura: '))
imc = peso/pow(altura,2)
print('Sua altura é {:.2f}, seu peso {:.1f}Kg e seu Índice de Massa Corporal é {:.1f}'.format(altura,peso,imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc <=25:
     print('Peso ideal')
elif imc <=30:
     print('Sobrepeso')
elif imc <=40:
     print('Obesidade')
else:
     print('Obesidade Mórbida')