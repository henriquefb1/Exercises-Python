# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

count = 0
number_sum = 0
list_number = []


while True:
    number = int(input('Valor: '))
    count += 1
    number_sum += number
    list_number.append(number)
    choice = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if choice == 'N':
        break


sorted(list_number)
print(f'De todos os valores digitados, a média foi {(number_sum / count):.2f}. \nO maior valor foi {list_number[0]} e o menor valor foi {list_number[-1]}.')