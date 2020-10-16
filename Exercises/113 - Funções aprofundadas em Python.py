# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception:
            print('ERRO! Favor digitar um valor inteiro em forma numérica (Ex: 7).')
            continue
        else:
            return n



def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception:
            print('ERRO! Favor digitar um valor real em forma numérica, utilizando ponto ao invés de vírgula (Ex: 5.5).')
            continue
        else:
            return n


num = leiaint('Digite um valor inteiro: ')
num2 = leiareal('Digite um valor real:')
print(f'O valor inteiro digitado foi {num} e o valor real foi {num2}.')