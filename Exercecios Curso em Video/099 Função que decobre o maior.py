'''
Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
'''



from time import sleep
n = 0
def maior(*num):
    print('-=' * 40)
    print('Analizando valores passados...')
    for c in num:
        print(c , end=' ', flush=True )
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo. ')
    for c in num:
        if c > n:
            n = c
    print(f'O maior valor iformado foi {n}')


maior(2, 9, 4, 5, 7, 1)
maior()