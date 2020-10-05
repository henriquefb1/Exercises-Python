# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

adult = 0
not_adult = 0

for c in range(0,7):
    birth = int(input('Qual o seu ano de nascimento?'))
    age = datetime.now().year - birth
    if age >= 18:
        adult += 1
    else:
        not_adult += 1

print(f'Dos 7 candidatos, a quantidade de adultos é {adult} e de jovens é {not_adult}.')
