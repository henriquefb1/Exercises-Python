# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = {}
score = []
total = 0

player['Name'] = str(input('Nome do jogador: ')).capitalize().split()
player['Matches'] = int(input('Quantas partidas jogadas? '))
for n, c in enumerate(range(0, player['Matches'])):
    point = int(input(f'Quantidade de gols na partida {n+1}: '))
    score.append(point)
    total += point

player['ScorePerMatch'] = score
player['TotalScore'] = total

