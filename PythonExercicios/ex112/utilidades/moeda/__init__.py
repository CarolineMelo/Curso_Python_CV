def aumentar(valor = 0, taxa = 0, formato= False):
 
  """_Calcula o aumento de um determinado preço_

  Param:
    valor (int, optional): _O valor a ser reajustado_. Defaults to 0.
    taxa (int, optional): _qual é a porcentagem de aumento_. Defaults to 0.
    formato (bool, optional): _deseja formatar a saída ou não_. Defaults to False.

  Returns:
    _type_: _o valor reajustado, com ou sem formatação_
  """
  resultado =  valor + (valor * taxa/100)
  return resultado if formato is False else moeda(resultado)

def diminuir(valor = 0, taxa = 0, formato=False):
    
  resultado = valor - (valor * taxa/100)
  return resultado if formato is False else moeda(resultado)



def dobro(valor = 0, formato = False):
  resultado =  valor * 2
  return resultado if not formato else moeda(resultado)


def metade(valor = 0, formato = False):
  resultado = valor / 2
  return resultado if formato is False else moeda(resultado)


def moeda(valor = 0, moeda = 'R$'):
  return f'{moeda}{valor:8.2f}'.replace('.',',')


def resumo(valor = 0, taxaa=10, taxadim=5):
  print('-='* 30)
  print('RESUMO DO VALOR'.center(30))
  print('-='* 30)
  print(f'Preço analisado:\t{moeda(valor)}')
  print(f'Metade do preço:\t{metade(valor, True)}')
  print(f'Dobro do preço:\t\t{dobro(valor, True)}')
  print(f'{taxaa}% de aumento: \t{aumentar(valor,taxaa, True)}')
  print(f'{taxadim}% de redução: \t{diminuir(valor,taxadim, True)}')
  print('-='* 30)