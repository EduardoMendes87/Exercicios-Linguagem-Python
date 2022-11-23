# crie um programa que leia um numeor real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um numero: '))
print(f'O valor digitador foi {num} e a sua parte inteira é {trunc(num)}')
