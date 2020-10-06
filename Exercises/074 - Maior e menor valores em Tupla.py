# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numbers = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Os números gerados foram {numbers}. \nO maior valor foi {max(numbers)}. \nO menor valor foi {min(numbers)}.')