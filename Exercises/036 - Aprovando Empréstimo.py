#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Valor do imóvel: R$'))
salary = float(input('Salário do comprador: R$'))
years = int(input('Quantidade de parcelas(anos): '))
months = years * 12
payments = house_value / months

if payments > (salary * 0.30):
    print('Infelizmente seu pedido de empréstimo foi negado, pois a prestação mensal excedeu 30% de seu salário, favor tentar novamente com outras especificações.')
else:
    print(f'Pedido de empréstimo aprovado para um imóvel no valor de R${house_value:.2f}, para pagamento em {years} anos, com prestações no valor de R${payments:.2f} por mês.')



