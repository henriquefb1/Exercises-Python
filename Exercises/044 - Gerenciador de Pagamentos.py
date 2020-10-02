#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

price = float(input('Favor informar o valor da mercadora: R$'))

payment_method = int(input('Favor escolher umas da opções de pagamento de acordo com o número de cada uma. \n1: À vista dinheiro/cheque: 10% de desconto. \n2: À vista no cartão: 5% de desconto. \n3: Em até 2x no cartão: preço formal. \n4: 3x ou mais no cartão: 20% de juros. \nOPÇÃO DE ESCOLHA(Ex: 2):  '))

if payment_method == 1:
    new_price = price * 0.90
    print(f'Optando por pagamento à vista dinheiro/cheque, você recebe 10% de desconto com um valor total de: R${new_price:.2f}.')
elif payment_method == 2:
    new_price = price * 0.95
    print(f'Optando por pagamento à vista no cartão, você recebe 5% de desconto com um valor total de: R${new_price:.2f}.')
elif payment_method == 3:
    print(f'Optando por pagamento em 2x no cartão, você recebe o valor formal da mercadoria em 2 parcelas de R${(price/2):.2f}.')
elif payment_method == 4:
    new_price = price * 1.20
    print(f'Optando por pagamento em 3x ou mais (Max: 6x), você recebe um juros total de 20% no valor da mercadoria, com um valor final de R${new_price:.2f}.')
    installments = int(input('Em quantas vezes gostaria de pagar(3-6)?: '))
    print(f'Optando por {installments} parcelas, cada parcela fica no valor de R${(new_price / installments):.2f}.')