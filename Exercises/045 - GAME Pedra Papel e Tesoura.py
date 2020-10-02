# 045: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print(f'Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
player_choice = int(input('Qual é a sua jogada?'))
computer_choice = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-'*10)
if player_choice == 0:
    if computer_choice == 0:
        print(f' Computador jogou PEDRA e você jogou PEDRA. EMPATE!!!')
    elif computer_choice == 1:
        print(f'Computador jogou PAPEL e você jogou PEDRA. Computador GANHOU!!!')
    else:
        print(f'Computador jogou TESOURA e você jogou PEDRA. Você GANHOU!!!')
elif player_choice == 1:
    if computer_choice == 0:
        print(f'Computador jogou PEDRA e você jogou PAPEL. Você GANHOU!!!')
    elif computer_choice == 1:
        print(f'Computador jogou PAPEL e você jogou PAPEL. EMPATE!!!')
    elif computer_choice == 2:
        print(f'Computador jogou TESOURA e você jogou PAPEL. Computador GANHOU!!!')
elif player_choice == 2:
    if computer_choice == 0:
        print(f'Computador jogou PEDRA e você jogou TESOURA. Computador GANHOU!!!')
    elif computer_choice == 1:
        print(f'Computador jogou PAPEL e você jogou TESOURA. Você GANHOU!!!')
    elif computer_choice == 2:
        print(f'Computador jogou TESOURA e você jogou TESOURA. EMPATE!!!')
print('-=-'*10)