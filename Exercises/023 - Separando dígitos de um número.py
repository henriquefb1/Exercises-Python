# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. (Solução com IFs, pode ser feito também igualando valores, como por sempre if num < 100, if number < 1000 , etc.)

num = str(input('Digite qualquer número entre 0 e 9999: '))

if len(num) == 4:
    unidade = num[3]
    dezena = num[2]
    centena = num[1]
    milhar = num[0]
    print(f'O valor é representado da seguinte maneira: \nUnidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
elif len(num) == 3:
    unidade = num[2]
    dezena = num[1]
    centena = num[0]
    milhar = 'Não existente'
    print(f'O valor é representado da seguinte maneira: \nUnidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
elif len(num) == 2:
    unidade = num[1]
    dezena = num[0]
    centena = 'Não existente'
    milhar = 'Não existente'
    print(f'O valor é representado da seguinte maneira: \nUnidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
elif len(num) == 1:
    unidade = num[0]
    dezena = 'Não existente'
    centena = 'Não existente'
    milhar = 'Não existente'
    print(f'O valor é representado da seguinte maneira: \nUnidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')
