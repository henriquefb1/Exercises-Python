#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

number_1 = int(input('Primeiro valor: '))
number_2 = int(input('Segundo valor: '))

while True:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    choice = int(input('Qual a sua opção? '))
    if choice == 1:
        print(f'O resultado de {number_1} + {number_2} é {(number_1 + number_2)}.')
    elif choice == 2:
        print(f'O resultado de {number_1} * {number_2} é {(number_1 * number_2)}.')
    elif choice == 3:
        if number_1 > number_2:
            print(f'O maior valor entre {number_1} e {number_2} é {number_1}.')
        elif number_2 > number_1:
            print(f'O maior valor entre {number_1} e {number_2} é {number_2}.')
        elif number_1 == number_2:
            print(f'Ambos os valores são iguais.')
    elif choice == 4:
        number_1 = int(input('Favor informar o seu primeiro novo valor: '))
        number_2 = int(input('Segundo novo valor: '))
    elif choice == 5:
        print('Você optou por sair do programa.')
        break

