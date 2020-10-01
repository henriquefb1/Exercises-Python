#  Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

number = int(input('Olá! Digite um número inteiro e faremos a tabuada para você!: '))


print('-=-'*5)

for c in range(1,11):
    print(f'{number} * {c} = {number * c}')

print('-=-'*5)