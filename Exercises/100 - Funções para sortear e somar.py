# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia(lista):
    from random import randint
    for _ in range(0,5):
        lista.append(randint(0,100))
    print(lista)
    
    

def somaPar(lista):
    c = 0
    for n in lista:
        if n % 2 == 0:
            c += n
    print(c)
            

números = []
sorteia(números)
somaPar(números)






