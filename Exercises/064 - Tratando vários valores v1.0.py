# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

number_count = 0
number_sum = 0


while True:
    number = int(input('Informar valor[999 para parar]: '))
    if number == 999:
        break
    else:
        number_count += 1
        number_sum += number

if number_count > 1:
    print(f'Você digitou {number_count} números, com uma soma total de {number_sum}.')
elif number_count == 0:
    print('Você não digitou qualquer número.')
elif number_count == 1:
    print(f'Você apenas digitou {number_count}, sendo esse {number_sum}.')