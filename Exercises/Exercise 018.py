# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
num = float(input('Digite o ângulo: '))

valor = math.radians(num)

sen = math.sin(valor)
cos = math.cos(valor)
tang = math.tan(valor)

print(f'Seno:{sen:.2f} \n Cosseno:{cos:.2f} \n Tangente:{tang:.2f}')