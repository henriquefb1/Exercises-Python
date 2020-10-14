# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

students = []

while True:
    name = str(input('Nome do aluno: ')).upper().strip()
    grade_1 = float(input('Nota 1: '))
    grade_2 = float(input('Nota 2: '))
    average = (grade_1 + grade_2) / 2
    students.append([name, average, grade_1, grade_2])
    choice = str(input('Deseja continuar? S/N: ')).upper().strip()
    if choice == 'N':
        break

print('No. Nome. Média.')
for n, s in enumerate(students):
    print(n, s[0], s[1])

while True:
    grades = int(input('Mostrar notas de qual aluno? [999 para encerrar]  '))
    print(f'Notas de {students[grades][0]} são {students[grades][2]} e {students[grades][3]}.')
    if grades == 999:
        break

print('Sistema finalizado.')