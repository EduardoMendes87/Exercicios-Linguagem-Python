'''
Escreva um programa que pergunte o salario de um funcionario e 
calcule o valor de seu aumento.
Para salarios superiores a R$ 1250,00, calcule um aumento de 10%
Para os inferiores ou iguais , o aumento é de 15%.
'''
from colorama import Fore, init
init(autoreset=True)

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    reajuste = salario + (salario * 15 / 100)
else:
    reajuste= salario + (salario * 10 / 100)
print('Quem ganhava R$ ' + Fore.RED + f'{salario:.2f}', 'passa a ganha R$', Fore.GREEN + f'{reajuste:.2f}')