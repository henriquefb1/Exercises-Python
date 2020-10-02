# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

number = 0

while number != 51:
    number += 1
    if number % 2 == 0:
        print(number)
    sleep(0.3)