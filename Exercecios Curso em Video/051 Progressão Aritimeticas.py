'''
Desenvola um programa que leia o primeiro termo e a razão
de uma PA. no fina, mostre os 10 primeiros termos dessa progressão
'''


print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for n in range(termo, decimo + razao, razao):
    print(n, end='-> ')
print('ACABOU')