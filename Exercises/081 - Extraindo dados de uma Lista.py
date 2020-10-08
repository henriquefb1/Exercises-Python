# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numbers = []

while True:
    numbers.append(int(input('Digite um valor: ')))
    choice = str(input('Deseja continuar? [S/N]: ')).upper()
    if choice == 'N':
        break

print(f'Quantidade de números digitados: {len(numbers)}.')
print(f'Lista em ordem decrescente: {sorted(numbers, reverse=True)}.')
if 5 in numbers:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado nessa lista.')
