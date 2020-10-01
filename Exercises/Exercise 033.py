# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

lista = [num1, num2, num3]
lista.sort()

print(f'O maior número é {lista[-1]} e o menor número é {lista[0]}.')

