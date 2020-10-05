# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

message = str(input('Digite uma frase qualquer: ')).upper().replace(' ',"")


if message == message[::-1]:
    print(f'{message} é um palíndromo.')
else:
    print(f'{message} não é um palíndromo.')