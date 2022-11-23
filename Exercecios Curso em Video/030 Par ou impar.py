'''
crie um programa que leia um numero inteiro
e mostre na tela se ela e PAR ou IMPAR
'''

from colorama import Fore, init
init(autoreset=True)
num = int(input(Fore.MAGENTA + 'Me diga um numero qualquer: '))
if num % 2 == 0:
    print(Fore.WHITE + f'O número {num} é ' + Fore.GREEN + ' PAR')
else:    
    print(Fore.WHITE + f'O número {num} é',  Fore.GREEN + ' IMPAR')