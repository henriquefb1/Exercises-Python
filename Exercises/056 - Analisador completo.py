# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

age_total = 0
age_man = 0
oldest_man = None
young_ladies = 0


for c in range(1,5):
    name = str(input(f'Nome da {c}° pessoa: '))
    age_check = int(input(f'Idade da {c}° pessoa: '))
    gender = str(input(f'Sexo da {c}° pessoa: [M/F]: '))
    age_total += age_check
    if gender == 'M':
        if age_check > age_man:
            age_man = age_check
            oldest_man = name
    elif gender == 'F':
        if age_check < 20:
            young_ladies += 1


average_age = age_total / 4

print(f'A média de idade dos participantes é {average_age:.0f}. \nO homem mais velho é o {oldest_man}. \nEntre todas as participantes mulheres, a quantidade de participantes mais jovens do que 20 anos é {young_ladies}.')


    
