# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    num = int(input('Valor para tabuada[Digitar valor negativo para sair]: '))
    if num < 0:
        print('Você digitou um valor negativo e optou por sair.')
        break
    for c in range(1,11):
        print(f'{num} * {c} = {(num * c)}')
    