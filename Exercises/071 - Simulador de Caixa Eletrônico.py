# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

bill_50 = 0
bill_20 = 0
bill_10 = 0
bill_1 = 0

cash = int(input('Olá, favor informar valor para saque: '))


while cash > 0:
    if cash > 50:
        cash -= 50
        bill_50 += 1
    elif cash > 20:
        cash -= 20
        bill_20 += 1
    elif cash > 10:
        cash -= 10
        bill_10 += 1
    elif cash > 1:
        cash -= 1
        cash += 1

print(f'Foram sacadas as seguintes notas: \nR$50: {bill_50} \nR$20: {bill_20} \nR$10: {bill_10} \nR$1: {bill_1}')