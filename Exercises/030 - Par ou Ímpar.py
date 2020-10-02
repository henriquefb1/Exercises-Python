# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Olá! Digite um número inteiro e te direi se é PAR ou ÍMPAR: '))

if number % 2 == 0:
    print(f'O número {number} é PAR.')
else:
    print(f'O número {number} é ÍMPAR.')