# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

weight_list = []

for c in range(1,6):
    weight = float(input(f'Peso da {c}° pessoa: '))
    weight_list.append(weight)

weight_list.sort()
print(f'O maior peso foi: {weight_list[0]:.2f}Kg. \nO menor peso foi: {weight_list[-1]:.2f}Kg.')