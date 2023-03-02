'''Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.'''

'''
try:                 (tente)
    operação
except:              (exceção)
    falou
else:                 (é opcional)
    deu certo
finally:
    certo ou errado   (é opcional)
'''
'''try: 
    a = int(input('Número: '))
    b = int(input('Denominador: '))
    r = a / b 
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigada.')'''



try: 
    a = int(input('Número: '))
    b = int(input('Denominador: '))
    r = a / b 
except (ValueError, TypeError):
    print(f'Problema com os tipos de dados digitados')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigada.')