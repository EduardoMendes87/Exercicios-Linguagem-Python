'''
Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
'''



from time import sleep

def maior(* num):
    cont = m = 0
    print('-=' * 40)
    print('Analizando valores passados...')
    for c in num:
        print(c , end=' ', flush=True )
        sleep(0.3)
        if cont == 0:
            m = c
        else:
            if c > m:
                m > c
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')    
    print(f'O maior valor iformado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()