# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    age = datetime.today().year - ano
    if age < 18:
        print('Situação de voto: NEGADO')
    elif age < 70:
        print('Situação de voto: OBRIGATÓRIO')
    elif age > 70:
        print('Situação de voto: OPCIONAL')


voto(1992)