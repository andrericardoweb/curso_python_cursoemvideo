# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugados? '))
km_rodados = eval(input('Quantos Km rodados? '))
total_a_pagar = (dias * 60) + (km_rodados * 0.15)
print(f'O total a pagar é de R${total_a_pagar:.2f}')