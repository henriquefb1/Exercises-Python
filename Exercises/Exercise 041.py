# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import datetime

current_year = datetime.now().year
year_birth = int(input('Favor informar seu ano de nascimento: '))
age = current_year - year_birth

if age <= 9:
    print(f'Com {age} anos de idade, sua categoria é MIRIM.')
elif age <= 14:
    print(f'Com {age} anos de idade, sua categoria é INFANTIL.')
elif age <= 19:
    print(f'Com {age} anos de idade, sua categoria é JÚNIOR.')
elif age <=25:
    print(f'Com {age} anos de idade, sua categoria é SÊNIOR.')
else:
    print(f'Com {age} anos de idade, sua categoria é MASTER.')