# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo.

object = input('Olá! Digite algo, pode ser palavra, número inteiro ou não(Lembre de usar . e não ,) , use letras do tipo que quiser, espaço ou não, agora é contigo!: ')

print('Um pequeno guia para você :) : STR = Strings, palavras em geral, como texto. / INT = Número inteiros. / FLOAT = Número flutuantes, separados por um ponto. e BOOL = Valor lógico, separados entre TRUE e FALSE.')

print(f'O objeto em questão é do tipo primitivo {type(object)}.')
