'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

'''def mostraLinha():
    print('-'*30)

print('        SISTEMA DE ALUNOS          ')
mostraLinha()

def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
título('Curso em vídeo')    
título('Carol')    
título('Oi')'''    

'''def soma(a,b):
    s = a + b
    print(s)

#Programa principal
soma(4,5)
soma(8,9)
soma(2,1)
soma(a=5,b=4)'''

# def contador(*núm):
#     # print(núm)
#     for valor in núm:
#         print(f'{valor} ', end='')
#     print('FIM!')
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)

''' Esse é um exemplo de uma função em Python que utiliza o recurso de parâmetros variáveis *args. Quando definimos uma função com *args, estamos permitindo que ela receba um número indefinido de argumentos.'''

# def contador(*núm):
#     tam = len(núm)
#     print(f'Recebi os valores {núm} e são ao todo {tam} números')
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)

'''Em Python, é possível definir funções que recebam um número variável de argumentos através do uso do caractere "*" antes do nome do parâmetro. Isso permite que a função possa receber um número indefinido de argumentos durante a sua chamada.

O caractere "" utilizado antes do nome do parâmetro é chamado de "operador de desempacotamento" e permite que a função receba um número variável de argumentos. Esses argumentos são agrupados em uma tupla (um tipo de objeto do Python que armazena uma sequência imutável de valores) e podem ser acessados dentro da função por meio do nome do parâmetro que foi definido com o operador "".

Por exemplo, na função "contador" definida no exemplo anterior, o parâmetro "*núm" é utilizado para receber um número indefinido de argumentos, que serão agrupados em uma tupla e armazenados na variável "núm".

Dessa forma, podemos chamar a função "contador" passando quantos argumentos quisermos, sem precisar especificar um número fixo de parâmetros. Isso oferece maior flexibilidade para a utilização da função e torna o código mais genérico e reutilizável.'''
'''Exemplo de desempacotamento:'''

# def soma(*valores):
#     s = 0
#     for num in valores:
#         s +=num
#     print(f'Somando os valores {valores} temos {s}')

# soma(5,2)
# soma(2,9,4)






####################################################################################################################
'''Quando se passa uma variável a uma função, o python passa a referência ao objeto ao qual a variável se refere (o valor), e não a variável propriamente dita ( obs: diferente de Java)'''
def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao]*=2
        posicao +=1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)

