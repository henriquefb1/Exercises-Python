# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

timer = 10

print('CONTAGEM REGRESSIVA PARA OS FOGOS!')

while timer != 0:
    print(timer,'!')
    timer -= 1
    sleep(1)

print('FELIZ ANO NOVO!!!')