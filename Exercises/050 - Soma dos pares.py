# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

for c in range (1,7):
    num = int(input('Digite um valor: '))
    total_sum = 0
    if num % 2 == 0:
        total_sum += num

print(f'A soma dos valores pares é {total_sum}.')

