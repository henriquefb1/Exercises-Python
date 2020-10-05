# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
 

total_price = 0
expensive = 0


while True:
    product = str(input('Nome do produto: ')).upper().strip()
    price = float(input('Preço do produto: R$'))
    total_price += price
    
    if price > 1000:
        expensive += 1
    
    choice = str(input('Deseja continuar?[S/N] ')).upper().strip()
    
    if choice == 'N':
        print(f'A) Total gasto na compra: R${total_price:.2f}. \nB)Quantidade de produtos que custam mais de R$1000: {expensive}.')
        break
    