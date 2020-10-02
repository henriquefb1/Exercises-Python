# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

weight = float(input('Favor informar seu peso(Ex: 87.50): '))
height = float(input('Favor informar sua altura em metros(Ex: 1.85): '))
imc = weight / (height * height)

if imc < 18.5:
    print(f'IMC: {imc:.2f}, SITUAÇÃO: ABAIXO DO PESO.')
elif imc < 25:
    print(f'IMC: {imc:.2f}, SITUAÇÃO: PESO IDEAL.')
elif imc < 30:
    print(f'IMC: {imc:.2f}, SITUAÇÃO: SOBREPESO.')
elif imc < 40:
    print(f'IMC: {imc:.2f}, SITUAÇÃO: OBESIDADE.')
else:
    print(f'IMC: {imc:.2f}, SITUAÇÃO: OBESIDADE MÓRBIDA.')