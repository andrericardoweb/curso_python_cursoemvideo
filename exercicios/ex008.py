# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = eval(input('Uma distância em metros: '))
print('CONVERTENDO MEDIDAS')
print(f'{m/1000}km | {m/100}hm | {m/10}dam | {m}m | {m*10}dm | {m*100}cm |{m*1000}mm')
