# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 

from random import randint
game = []
player = {}

for g in range(0,4):
    player['Nome'] = str(input('Nome do jogador: ')).upper().split()
    print(f'Jogador(a) {player["Nome"]} cadastrado(a).')
    player['Jogada'] = randint(1,6)
    print(f'Jogou.....{player["Jogada"]}.')
    game.append(player.copy())



print(game)
