# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Olá! bem-vindo ao sistema de devolução e pagamento do aluguel do seu carro, para finalizarmos o processo, precisaremos saber a quantidade de KMs percorridos e dias alugados.')
kms = float(input('Favor informar quantos KMs foram percorridos: '))
days = int(input('Agora quantos dias o carro foi alugado: '))
price_kms = kms * 0.15
price_days = days * 60
total = price_days + price_kms

print(f'Muito bem! Primeiramente, o nosso preço por KM é de R$0.15, como foram percorridos {kms:.2f}KMs, o preço de KMs fica em R${price_kms:.2f} e para cada dia alugado é cobrado R$60.00, nesse caso pelo período de {days} dias, resultou em um total de R${price_days:.2f} para a quantidade de dias alugado.')
print(f'O valor total de seu aluguel ficou: R${total:.2f}. Esperamos que nosso serviço tenha sido satisfatório, estamos à sua disposição para qualquer assunto ou problema.')
