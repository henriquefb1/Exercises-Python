# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

people = []
women = []
above_average = []
person = {}

counter = 0
age_counter = 0


while True:
    person['Name'] = str(input('Nome: ')).capitalize().split()
    person['Gender'] = str(input('Sexo: [F/M] ')).upper().split()
    person['Age'] = int(input('Idade: '))
    counter += 1
    age_counter += person['Age']
    people.append(person.copy)
    if person['Gender'] == 'F':
        women.append(person.copy)
    choice = str(input('Deseja continuar? [S/N] ')).upper().split()
    if choice == 'Nn':
        break


average_age = age_counter / counter


for k in people:
    if person['Age'] > average_age:
        above_average.append(person.copy)


print(f'A) Foi cadastrado um total de {counter} pessoas.')
print(f'B) A média de idade é {average_age}.')
print(f'C) As mulheres do grupo são {women}.')
print(f'D) As pessoas acima da média da idade são {above_average}')