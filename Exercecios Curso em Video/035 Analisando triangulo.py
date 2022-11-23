'''
Desenvolva um programa que leia o comprimento 
de tres retas e diga ao usuario se ela podem ou nao
formar um triangulo
'''
from colorama import Fore, init
init(autoreset=True)
print(Fore.GREEN +'-=' * 20)
print(' ' * 7, Fore.RED + 'Analizador de Triâmgulos')
print(Fore.GREEN + '-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR trinagulo')

