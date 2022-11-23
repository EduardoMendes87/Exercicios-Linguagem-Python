'''
Faça um programa que leia um numero inteiro
e diga se ele é ou não um numero primo
'''

from colorama import Fore, init
init(autoreset=True)

num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:           
        cont += 1
    print(c, end=' ')
print(f'\nO numero {num} foi divisivel {cont} vezes.')
if cont == 2:
    print('E por isso ele é um numero PRIMO!!!')
else:
    print('E por isso ele não é um número PRIMO!!!')   