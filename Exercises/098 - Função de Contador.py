# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar duas contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2


from time import sleep

def contador(start, end, tick):
    print(f'Contagem de {start} até {end} de {tick} em {tick}.')
    if start < end:
        for c in range(start, end+1, tick):
            print(f'{c}',end=' ')
        print('FIM!')
            
    elif start >= end:
        while start > end:
            print(f'{start}', end=' ')
            start -= tick
        print('FIM!')


contador(1, 10, 1)

contador(10, 0, 2)

