# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

count = 0
num_sum = 0

while True:
    num = int(input('Valor[999 para sair]: '))
    if num == 999:
        break
    count += 1
    num_sum += num
    

if count > 1:
    print(f'Foram informados {count} valores, com uma soma total de {num_sum}.')
elif count == 1:
    print(f'Foi informado apenas 1 valor: {num_sum}.')
elif count == 0:
    print(f'Nenhum valor foi informado.')

