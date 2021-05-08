# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valor = eval(input('Quanto dinheiro você tem na carteira? R$: '))
cotacao_dolar = 5.24
print(f'Com R${valor:.2f} você pode comprar US${valor/cotacao_dolar:.2f}')