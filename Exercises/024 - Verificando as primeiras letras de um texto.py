# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Em que cidade você nasceu?')).upper().split()
check = ('SANTO' == cidade[0])
if check == False:
    print('O nome da sua cidade não começa com SANTO.')
else:
    print('O nome da sua cidade começa com SANTO! :)')