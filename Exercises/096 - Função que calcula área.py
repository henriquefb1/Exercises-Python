# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(a, b):
    total = a * b
    print(f'Área total do terreno: {total}M².')


print(f'Olá, vamos calcular a área do seu terreno!')
l = float(input('Favor informar a largura do terreno(M): '))
c = float(input('Agora informar o comprimento do terreno(M): '))
área(l, c)
