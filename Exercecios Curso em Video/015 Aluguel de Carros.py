# escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. calcule o preço a pagar, sabendo que o carros
# custa R$60 por dia e R0.15 por km rodado.

dias = int(input('Quantos dias rodados? '))
km = float(input('Quantos Km rodados? '))
valor = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${valor:.2f}.')
