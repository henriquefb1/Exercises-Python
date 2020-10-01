# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('Olá viajante! Sabemos que as temperaturas são calculadas em Fahrenheit na Inglaterra, por isso estamos prontos para calcular para você a mesma temperatura em Celsius!')
fahrenheit = int(input('É só nos informar a temperatura e faremos a conversão para você: '))
celsius = (fahrenheit - 32) / 1.8

print(f'Pronto! {fahrenheit} Fahrenheit é nada mais e nade menos que {celsius:.2f} Celsius, esperamos ter ajudado, sempre que precisar é só nos informar a temperatura e o resto é com a gente.')
