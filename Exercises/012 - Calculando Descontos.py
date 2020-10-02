#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Olá! favor informar o valor da mercadoria para que possamos aplicar o desconto de acordo: R$'))
new_price = price * 0.95
difference = price - new_price

print(f'Muito bem, o seu produto acaba de receber um desconto de 5%!, uma redução de R${difference}, o valor para ser pago é R${new_price}.')
print('Muito obrigado por escolher as lojas Guanabara, faça o download de nosso APP para ficar por dentro de todos os descontos e promoções! Baixe agora o Guanabara Shop App na Apple Store ou Play Store.')
