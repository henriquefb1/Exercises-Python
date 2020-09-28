# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

grade_1 = float(input('Favor informar a primeira nota do aluno(a): '))
grade_2 = float(input('Agora a segunda nota: '))
average = (grade_1 + grade_2) / 2

print(f'Com uma nota de {grade_1} e {grade_2}, o aluno(a) ficou com uma média de {average}.')