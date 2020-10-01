# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

number = int(input('Olá olá! Digite um valor inteiro e iremos calcular o dobro, triplo e raiz quadrade para você!: '))
double = number * 2
triple = number * 3
square_root = int(sqrt(number))

print(f'Muito bem, para o número {number} conseguimos o seguinte: dobro:{double}, triplo:{triple} e raiz quadrada:{square_root}.')
