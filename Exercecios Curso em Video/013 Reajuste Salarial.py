# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario =  float(input('Qual é o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${reajuste:.2f}')
