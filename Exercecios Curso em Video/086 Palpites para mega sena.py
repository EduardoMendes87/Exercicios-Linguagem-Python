'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O
programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
numsorteados = []
print('-'*30)
print(' '*6, 'JOGO DA MEGA SENA')
print('-'*30)
quantjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3,f'SORTEANDO {quantjogos} JOGOS', '-='*3)
sleep(1)
for c in range(1, quantjogos + 1):
    for i in range(1, 7):
        computador = randint(1, 60)       
        numsorteados.append(computador)
    print(f'Jogo {c}: {numsorteados}')
    sleep(0.5)
    numsorteados.clear()
print('-='*5, 'BOA SORTE', '-='*5)



# SOLUÇÃO DO GUANABARA - MEU CÓDIGO NÃO VERIFICAVA SE O NUMERO SORTEADO ERA REPTIDO
'''
from random import randit
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGOS NA MEGA SENA      ')
print('-'*30)
quant =  int(input('Quantos jogos vecê quer que eu jogue? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randit(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'BOA SORTE', '-='*5)




'''