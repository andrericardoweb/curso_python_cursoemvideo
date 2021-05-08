# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura_parede = eval(input('Largura da parede: '))
altura_parede = eval(input('Altura da parede: '))
area = largura_parede * altura_parede
qntd_tinta = area / 2
print(f'Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {qntd_tinta:.2f}l de tinta.')