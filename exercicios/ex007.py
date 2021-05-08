# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = eval(input('Primeira nota do aluno: '))
nota2 = eval(input('Segunda nota do aluno: '))
print(f'A média entre {nota1:.1f} e {nota2:.1f} é igual a {(nota1 + nota2)/2:.1f}')