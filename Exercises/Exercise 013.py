# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Olá colaborador(a)!, Favor informar seu salário para que possamos calcular seu reajuste anual: R$'))
new_salary = salary * 1.15
difference_salary = new_salary - salary

print(f'Muito bem! Você acabou de receber 15% de aumento no seu salário, umas de nossas maneiras de agradecer pelo seu ótimo serviço! O seu novo salário agora é R${new_salary:.2f}, um aumento de R${difference_salary:.2f}. Parabéns e juntos somos mais!')