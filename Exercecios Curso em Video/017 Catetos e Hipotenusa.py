'''
Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um 
triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
from math import hypot
oposto = float(input('Comprimento di cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
