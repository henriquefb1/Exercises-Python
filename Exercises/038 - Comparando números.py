# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input('Favor informar o primeiro número inteiro: '))
num2 = int(input('Favor informar o segundo número inteiro: '))

if num1 == num2:
    print(f'Ambos os valores digitados foram {num1}.')
elif num1 > num2:
    print(f'Entre os valores digitados, o primeiro é maior: {num1}.')
else:
    print(f'Entre os valores digitados, o segundo é maior: {num2}.')
    