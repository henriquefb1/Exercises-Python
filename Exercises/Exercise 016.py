# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

number = float(input("Favor digitar um número real, utilizando '.' ao invés de ',' : "))
print(f'A porção inteira do valor digitado é {int(number)}.') # Não arredonda
print(f'A porção inteira do valor digitado é {number:.0f}.')  # Arredonda