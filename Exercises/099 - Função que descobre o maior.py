# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    from time import sleep
    print('-=-' * 20)
    print('Analisando valores....')
    sleep(1)
    for c in num:
        print(f'{c}', end=' ')
    print(f'/ Foram analisados um total de {len(num)} números.')
    new_num = list(num)
    new_num.sort(reverse=True)
    print(f'O maior valor foi {new_num[0]}.')


maior(5,1,10,9,8,7)