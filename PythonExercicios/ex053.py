# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

frase = str(input("Escreva uma frase: ")).strip().upper()#Remover espaço antes e depois/ passar tudo para maiúsculo.
palavras = frase.split()#dividir
junto = ''.join(palavras)#junte
inverso = junto[::-1]#fatiamento
print("O inverso de {} é {}".format(junto, inverso))

if junto != inverso:
 print("A frase digitada não é um palíndromo!")
else: 
  print("A frase digitada é um palíndromo!")



# print("Essa frase invertida é {}".format(palavras))
# print("Essa frase invertida é {}".format(junto))