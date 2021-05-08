# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))
print(f'O dobro de {numero} vale {numero * 2} \nO triplo de {numero} vale {numero * 3} \nA raiz quadrada de {numero} é igual a {(numero ** (1/2)):.2f}')