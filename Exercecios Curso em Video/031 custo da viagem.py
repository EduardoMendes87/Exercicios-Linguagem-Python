'''
Desenvolva um programa que pergunte a distancia de uma viagem
em km. calacule o preço da passagem cobrando R$0.50 por km para
viagems ate 200km e R$0.45 para viagens mais longas
'''

from time import sleep
km = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {km:.1f}km')
print('-=-' * 14)
print(' ' * 10, 'Agencia de Turismo')
print('-=-' * 14)
print('Aguarde calculando valora da passagem...')
sleep(2)
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print(f'E o preço da sua passagem será de R${valor:.2f}')
