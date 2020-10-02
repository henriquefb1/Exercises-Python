#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

grade_1 = float(input('Primeira nota: '))
grade_2 = float(input('Segunda nota: '))
average = (grade_1 + grade_2) / 2

if average < 5.0:
    print(f'Situação: REPROVADO, média: {average:.2f}.')
elif average < 7.0:
    print(f'Situação: RECUPERAÇÃO, média: {average:.2f}.')
else:
    print(f'Situação: APROVADO, média: {average:.2f}.')