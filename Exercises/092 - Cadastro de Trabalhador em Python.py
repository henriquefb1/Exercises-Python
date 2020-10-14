# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

worker = {}

worker['Name'] = str(input('Nome: '))
worker['YearOfBirth'] = int(input('Ano de nascimento: '))
worker['Age'] = datetime.datetime.now().year - worker['YearOfBirth']
worker['CTPS'] = int(input('Carteira de trabalho: '))
if worker['CTPS'] != 0:
    worker['YearOfHire'] = int(input('Ano de contratação: '))
    worker['Salary'] = float(input('Salário: '))
    worker['AgeOfRetirement'] = worker['Age'] - (datetime.datetime.now().year - worker['YearOfHire']) + 30
    print(f'{worker["Name"]}, idade: {worker["Age"]}, CTPS: {worker["CTPS"]}, ano de contratação: {worker["YearOfHire"]}, Salário: R${worker["Salary"]}, Idade de aposentadoria: {worker["AgeOfRetirement"]}.')

