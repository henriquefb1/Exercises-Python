# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

measure = float(input('Escreva uma medida em metros (Apenas números) e iremos fazer a conversão para centímetros e milímetros: '))
cm = measure * 100
mm = measure * 1000

print(f'Para {measure:.2f} metros, são {cm:.2f} centímetros e {mm:.2f} milímetros.')