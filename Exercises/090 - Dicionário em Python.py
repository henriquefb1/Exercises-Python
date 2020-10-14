# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

students = {}

name = str(input('Nome do aluno(a): ')).upper().split()
average = float(input('Média do aluno(a): '))
if average < 7.0:
    situation = 'REPROVADO'
else:
    situation = 'APROVADO'
students = {'Nome': name, 'Média': average, 'Situação': situation}

print(f'O aluno(a) {students["Nome"]} possui uma média de {students["Média"]} e sua situação é {students["Situação"]}.')