# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

gender = str(input('Favor informar seu sexo [M/F]: ')).upper().strip()

while gender != 'M' and gender != 'F':
    gender = str(input('Dados inválidos. Por favor, informe seu sexo corretamente. [M/F]: '))

print(f'Sexo [{gender}] cadastrado com sucesso!.')