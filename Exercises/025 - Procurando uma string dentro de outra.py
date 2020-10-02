# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Favor informar seu nome inteiro: ')).strip().upper().split()

for num, n in enumerate(name):
    check = ('SILVA' == name[num])
    if check == True:
        print('Seu nome tem "SILVA".')
        break
if check == False:
    print('Seu nome não tem "SILVA".')