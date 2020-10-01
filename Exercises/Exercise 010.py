# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Valor no dia 28/09/2020 = 5,62

wallet = float(input('Olá! Pensando em comprar uns dólares? É só informar quantos reais você quer trocar e calculamos tudo para você!: '))
usd = wallet / 5.62

print(f'Com {wallet:.2f} BRL você consegue {usd:.2f} USD. (BRL = Reais, USD = Dólares).')
