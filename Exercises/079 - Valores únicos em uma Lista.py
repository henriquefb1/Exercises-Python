# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

numbers = []
user = 0


while True:
    user = int(input('Digite um valor: '))
    if user in numbers:
        print('Valor repetido.')
    else:
        numbers.append(user)
    more = str(input('Deseja continuar? [S/N]: ')).upper()
    if more == 'N':
        break

print(f'Os valores digitados foram {sorted(numbers)}.')