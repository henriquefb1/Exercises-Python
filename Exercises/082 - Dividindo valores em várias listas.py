# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numbers = []
even = []
uneven = []
number = 0

while True:
    number = (int(input('Digite um valor: ')))
    numbers.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        uneven.append(number)
    choice = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if choice == 'N':
        break

print(f'Os valores digitados foram: {numbers}. \nOs valores pares são: {even}. \nOs valores ímpares são: {uneven}.')