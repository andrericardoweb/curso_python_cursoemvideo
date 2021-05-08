# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = eval(input('Qual é o salário do funcionário? R$ '))
aumento = salario * 1.15
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario * 1.15:.2f}')