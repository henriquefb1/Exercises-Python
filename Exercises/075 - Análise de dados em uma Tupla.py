# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.


numbers = []
countnine = 0

for c in range(0,4):
    numbers.append(int(input('Digite um valor: ')))

tuple(numbers)

for c in numbers:
    if c == 9:
        countnine += 1

print(f'Quantidade de 9: {countnine}.')

if 3 in numbers:
    print(f'O primeiro número 3 se encontra na posição {numbers.index(3)+1}.')
else:
    print('Não foi digitado qualquer número 3.')



        
