# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Salário: R$'))

if salary > 1250:
    new_salary = salary * 1.10
    print(f'Novo salário: R${new_salary:.2f}.')
else:
    new_salary = salary * 1.15
    print(f'Novo salário: R${new_salary:.2f}.')