# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

numbers = []

for c in range(0,5):
    numbers.append(int(input('Digite um valor:')))

print(f'O maior valor digitado foi: {max(numbers)}, na posição {numbers.index(max(numbers))}.')
print(f'O menor valor digitado foi: {min(numbers)}, na posição {numbers.index(min(numbers))}.')