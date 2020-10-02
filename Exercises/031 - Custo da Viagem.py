# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

trip = int(input('Favor informar a distância de sua viagem em KM: '))

if trip <= 200:
    print(f'O valor de sua viagem é de R${trip * 0.50:.2f}.')
else:
    print(f'O valor de sua viagem é de R${trip * 0.45:.2f}.')