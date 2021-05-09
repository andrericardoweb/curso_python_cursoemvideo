# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura_c = eval(input('Informe a temperatura em ºC: '))
temperatura_f = (temperatura_c * 1.8) + 32
print(f'A temperatura de {temperatura_c}ºC corresponde a {temperatura_f}ºF')