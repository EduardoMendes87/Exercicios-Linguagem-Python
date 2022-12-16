'''
Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(a, b):
    s = a * b
    print(f'A área de um terreno {a} x {b} é de {s:.2f}m')


print('Controle de Terrenos')
print('-' * 20)
larrgura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(a=larrgura, b=comprimento)

