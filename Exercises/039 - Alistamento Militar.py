# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

current_year = datetime.now().year

year = int(input('Ano de nascimento: '))

age = current_year - year

min_age = 18

print(f'Quem nasceu em {year} tem {age} anos de idade em {current_year}.')

if age < min_age:
    print(f'Ainda faltam {min_age - age} anos para seu alistamento. \nSeu alistamento será em {current_year + (min_age - age)}.')
elif age > min_age:
    print(f'Você já deveria ter se alistado há {age - min_age} anos. \nSeu ano de alistamento foi em {current_year - (age - min_age)}.')
