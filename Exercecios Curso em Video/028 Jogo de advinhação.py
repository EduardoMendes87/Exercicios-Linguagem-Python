'''
Escreva um programa que faça o computador "PENSAR" em um
numero inteiro entre 0 a 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador. o programa deverá
escrever na tela se o ussuario venceu ou perdeu
'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
print('Pensando...')
sleep(2)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print(f'PARABENS! Voçê conseguiu me vencer!!!')
else:
    print(f'GANHEI! Eu pensei no numero {computador} e não no {jogador}')





