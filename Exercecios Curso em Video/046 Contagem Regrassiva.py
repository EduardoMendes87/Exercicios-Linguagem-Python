'''
Faça um programa que mostre na tela uma contagem regressiva
para estrouro de fogos de artificios, indo de 10 ate 0,
com uma pausa de 1 segundo entre eles.
'''

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('=-'*13)
print('BUM!  BUM! POOOOOOWWWWWWW!')
print('=-'*13)
