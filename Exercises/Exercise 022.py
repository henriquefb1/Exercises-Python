# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).


name = str(input('Favor digitar seu nome inteiro para análise: '))
space = name.count(' ')

print(f'{name.upper()}')
print(f'{name.lower()}')
print(f'A quantidade de letras é {len(name) - space}')

