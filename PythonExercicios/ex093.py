# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogadores= {}
total_gols = list()
jogadores['nome'] = str(input('Nome do Jogador: '))
jogadores['qtd_partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))


for c in range(0,jogadores['qtd_partidas']):
    total_gols.append(int(input( f'Quantos gols na partida {c + 1}: ')))
jogadores['gol'] = total_gols[:] 

print('-='*40)
print(jogadores)
for k,v in jogadores.items():
    print(f'O campo {k} tem o valor {v}')


print('-='*40)
print(f'O jogador {jogadores["nome"]} jogou {jogadores["qtd_partidas"]} partidas.')
print('-='*40)

for i,v in enumerate(jogadores['gol']):
    print(f' => Na partida {i+1}, fez {v} gols')

print(f'Foi um total de {sum(total_gols)} gols.')