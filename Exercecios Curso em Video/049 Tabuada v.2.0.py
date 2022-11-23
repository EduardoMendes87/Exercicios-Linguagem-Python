'''
Refaça o desafio 009, mostrando a tabuada
de um numero que o usuario escolher,
so que agora utilizando um laço for.
'''

num = int(input('Digite um número para ver sua tabuada: '))
for n in range(1, 11):
    print(f'{num}  X  {n:2} = {num * n}')
