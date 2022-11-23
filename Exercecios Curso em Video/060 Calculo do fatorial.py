'''
Faça um programa que leia um número qualquer e mostre o seu fatorial:
EX:
5! = 5x4x3x2x1=0
'''

num = int(input('Digite um numero para\ncalacular seu Fatorial: '))
c = num
f = 1
print(f'Calaculando {num}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c> 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)