'''
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela
função anterior.
'''

from time import sleep
from random import randint
sorteados = list()
def sorteio():    
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        s = randint(1, 10)
        print(f'{s} ', end='', flush=True)
        sleep(0.3)
        sorteados.append(s)
    print('Pronto!!!')


def SomaPar():
    soma = 0
    print(f'Somando os valores pares de {sorteados}, ', end='')
    for c in sorteados:
        if c % 2 ==0:
            soma += c
    print(f'temos o total de {soma}.')



sorteio()
SomaPar()
