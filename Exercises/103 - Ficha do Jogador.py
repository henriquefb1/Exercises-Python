# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = 0, gols = 0):
    if nome == 0:
        sheet = (f'Nome do jogador: NÃO INFORMADO, gols marcados: {gols}.')
    elif gols == 0:
        sheet = (f'Nome do jogador: {nome}, gols marcados: 0/NÃO INFORMADO.')
    else:
        sheet = (f'Nome do jogador: {nome}, gols marcados: {gols}.')
    return sheet

