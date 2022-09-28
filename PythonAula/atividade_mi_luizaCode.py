#Crie um sistema de cadastro de pessoas, pelo nome e idade.


# nome = (input('Digite seu nome: '))
# idade = int(input('Digite sua idade: '))


listas = [[]] #uma lista de lista

while True:
    print("1-Cadastrar pessoa")
    print("2-Lista Cadastros")
    print("3-Sair")
    opcao = int(input())
    if opcao == 1:
        nova = []
        nome = input("Digite o nome da pessoa: ")
        idade = input("Idade da pessoa: ")
        
        nova.append(nome)
        nova.append(idade)
        listas.append(nova)

    elif opcao == 2:
        for registros in listas:
            for registros2 in registros:
                print(registros2)

    elif opcao == 3:
        print("Fim")