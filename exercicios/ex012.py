# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = eval(input('Qual é o preço do produto. R$'))
desconto_5perc = preco * 0.95
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${desconto_5perc:.2f}')