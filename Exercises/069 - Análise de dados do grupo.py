# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

adults = 0
male = 0
young_female = 0

while True:
    age = int(input('Idade: '))
    gender = str(input('Sexo[M/F]: ')).upper().strip()
    if age > 18:
        adults += 1
    if gender == 'M':
        male += 1
    if gender == 'F' and age < 20:
        young_female += 1
    choice = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if choice == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {adults}. \nTotal de homens: {male}. \nTotal de mulheres com menos de 20 anos de idade: {young_female}.')