# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

student_list = []

for s in range(0,4):
    student = str(input('Nome do aluno:'))
    student_list.append(student)

student_choice = random.choice(student_list)

print(f'O aluno escolhido foi: {student_choice}.')