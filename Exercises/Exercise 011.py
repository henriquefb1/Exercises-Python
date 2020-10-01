# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Olá! Vamos calcular quanta tinta você precisa para sua parede?')
largura = int(input('Favor primeiro informar a largura da parede em metros: '))
altura = int(input('Agora favor informar a altura em metros: '))
m2 = largura * altura
litragem = m2 / 2

print(f'Com uma largura de {largura}M e altura de {altura}M, sua parede possui uma área de {m2}M².')
print(f'Cada litro de nossa tinta cobre 2M², nesse caso você precisaria de {litragem} litros de tinta.')
print(f'Muito obrigado por optar pelas tintas Guanabara, favor notar que a quantidade de tinta necessária é baseado no uso de tinta Guanabara, não podemos certificar da quantidade exata para outras marcas.')
