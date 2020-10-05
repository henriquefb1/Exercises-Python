# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Olá novamente jogador(a)! Quero só ver quantas vezes vai precisar até acertar o número no qual estou pensando.')

number = randint(1,10)
tries = 0
attempt = None

while attempt != number:
    attempt = int(input('Palpite: '))
    tries += 1

print(f'Muito bem! Você acertou em {tries} tentativas! Eu estava pensando no número {number}.')
