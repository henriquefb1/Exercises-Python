# xercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

message = str(input('Olá! Favor informar a mensagem a qual gostaria de receber o tamanho adaptável de detalhes: '))
escreva(message)
