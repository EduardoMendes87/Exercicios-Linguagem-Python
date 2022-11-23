# Crie um programa que quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares pode comprar

saldo = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = saldo / 3.27
print(f'Com R${saldo:.2f} você pode comprar US${dolar:.2f}')
