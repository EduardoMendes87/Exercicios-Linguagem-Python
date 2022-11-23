'''
Escreva um programa para aprovar o emprestimo bancario para a 
compra de uma casa. Pergunte o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
A prestação mesal, não pode exceder 30% do salario ou entao o emprestimo sera negado.
'''

from colorama import Fore, init
init(autoreset=True)

casa = float(input('Valor da casa: R$  '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
parcela = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {casa:.2f} em {anos} a prestação será de R${parcela:.2f}')
if parcela <= minimo:
    print('Emprestimo pode ser', Fore.GREEN + 'CONCEDIDO', )
else:
    print('Emprestimo', Fore.RED + 'NEGADO', )
