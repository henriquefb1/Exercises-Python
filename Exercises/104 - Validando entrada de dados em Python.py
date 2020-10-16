# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg):
    ok = False
    value = 0
    while True:
        value = str(input(msg))
        if value.isnumeric():
            ok = True
        else:
            print('ERRO, a informação digitada não é um número inteiro.')
        if ok:
            break
    return value
   

n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')


