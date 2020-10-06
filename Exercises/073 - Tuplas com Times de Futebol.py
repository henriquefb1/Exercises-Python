#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Corinthians.

teams = ('Atlético-MG', 'Internacional', 'Palmeiras', 'Flamengo', 'Sport Recife', 'Santos', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Fortaleza', 'Atlético-GO', 'Athletico-PR', 'Ceará SC', 'Corinthians', 'Grêmio', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás')

print('Segue os 5 primeiros times: ')
for p, t in enumerate(range(0,5)):
    print(f'{p+1}:{teams[t]}')



print('Os 4 últimos colocados: ')
for c, d in enumerate(range(16,20)):
    print(f'{c+17}:{teams[d]}')


print('Tabela em ordem alfabética.')
print(sorted(teams))

print('Posição do Corinthians.')
print(f'O Corinthians se encontra na posição: {(teams.index("Corinthians")+ 1)}.')