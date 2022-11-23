'''
Refaça o desafio 0651, lendo o primeiro termo e a razão de uma PA.
mostrando os 10 primeiros termos da progressão ussando a estrutura while.
'''

print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont +=1
print('FIM!!!')