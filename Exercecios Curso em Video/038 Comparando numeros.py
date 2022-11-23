'''
Escreva um programa que leia dois numeros inteiros e compare-os
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais
'''

a = int(input('Primeiro númeor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('O PRIMEIRO valor é maior.')
elif b > a:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS')
