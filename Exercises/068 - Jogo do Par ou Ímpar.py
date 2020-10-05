#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

print('Vamos jogar par ou ímpar até você perder! Quero só ver quantas vezes você consegue ganhar ein!')

total_victories = 0

while True:
    num = int(input('Digite um valor: '))
    computer = randint(0,10)
    total = num + computer
    choice = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    if total % 2 == 0 and choice == 'P':
        print(f'Você escolheu {num} e o computador {computer}. Total de {total} deu PAR, MUITO BEM!')
        total_victories += 1
    elif total % 2 == 1 and choice == 'I':
        print(f'Você escolheu {num} e o computador {computer}. Total de {total} deu ÍMPAR, MUITO BEM!')
        total_victories += 1
    else:
        print(f'Você escolheu {num} e o computador {computer}. Total de {total}! PERDEU!')
        if total_victories == 0:
            print(f'Você ganhou um total de 0 vezes haha!, mais sorte na próxima!')
        elif total_victories == 1:
            print(f'Você ganhou apenas 1 vez.')
        else:
            print(f'Você ganhou um total de {total_victories} vezes.')
        break
