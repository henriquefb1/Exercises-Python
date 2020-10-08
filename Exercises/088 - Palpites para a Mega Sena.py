# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

lottery = []

attempts = int(input('Quantos jogos vocês gostaria de fazer? '))

for c in range(attempts):
    lottery.append(f'Jogo {c+1}: {[randint(1,60), randint(1,60), randint(1,60),randint(1,60), randint(1,60), randint(1,60)]}')

print(lottery)
