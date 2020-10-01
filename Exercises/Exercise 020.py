# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

student_list = []

for s in range(0,4):
    student = str(input('Nome do aluno(a): '))
    student_list.append(student)

random.shuffle(student_list)
print(f'A ordem para a apresentação é a seguinte: {student_list}.')
