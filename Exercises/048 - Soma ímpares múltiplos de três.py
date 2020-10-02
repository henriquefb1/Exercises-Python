# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

number = 0
counter = 0
total_sum = 0

while number < 501:
    number += 1
    if number % 3 == 0:
        counter += 1
        total_sum += number

print(f'A soma de todos os {counter} valores é {total_sum}.')

