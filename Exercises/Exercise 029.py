#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = int(input('Quantos Kms/h estava seu automóvel? '))
limit = 80


if speed > limit:
    diff = speed - limit
    fine = float(diff) * 7.00
    print(f'Você estava {diff}Kms/h além do limite de velocidade, resultando em uma multa no valor de R${fine:.2f}, favor digirir com mais segurança, seu papel é muito importante na sociedade. ')
else:
    print('Muito bem! Você não ultrapassou o limite de velocidade!')
