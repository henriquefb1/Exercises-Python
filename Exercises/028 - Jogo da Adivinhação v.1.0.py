#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('Olá! Vamos jogar um jogo? Irei pensar em um número entre 0 e 5 e você tenta descobrir qual foi o número que pensei....mas você possui apenas 1 chance!')

number = randint(0,5)

print('Estou pensando....')

sleep(1)

guess = int(input('Pronto! e agora é com você, em qual número eu estou pensando?'))

if number == guess:
    print(f'Muito bem! Eu estava pensando exatamente no número {number}.')
else:
    print(f'Há! Ganhei, eu estava pensando no número {number}.')

