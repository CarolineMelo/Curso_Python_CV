from time import sleep
number1 = int(input("Primeiro valor: "))
number2 = int(input("Segundo valor: "))
opcao =0

while opcao != 5:
  print( 
    '''
    Menu
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa'''
)
  opcao = int(input('Qual é a sua opção? '))
  if opcao == 1:
    soma = number1 + number2
    print('A soma entre {} e {} é {}'.format(number1,number2,soma))
  elif opcao == 2:
    produto = number1 * number2
    print('A multiplicação entre {} X {} é {}'.format(number1,number2,produto))

  elif opcao == 3:
    if number1 > number2:
     maior = number1
    else:
     maior = number2
    print(' Entre {} e {} o maior valor é {}'.format(number1,number2,maior))
  elif opcao == 4:
    print('Informe os números novamete:')
    number1 = int(input('Primeiro valor'))
    number2 = int(input('Segundo valor'))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida. Tente novamente')
  print('=-=-=' * 5)
  sleep(3)
print("Fim")

