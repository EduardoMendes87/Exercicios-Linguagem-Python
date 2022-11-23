'''
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato

'''


total = maior1000 = menovalor = 0
print('-' * 19)
print('Loja Super Baratão')
print('-' * 19)

while True:
    produto = str(input('Nome do Produto: '))
    preço =  float(input('Preço: R$ '))
    total += preço    
    if preço > 1000:
        maior1000 += 1 
    if menovalor == 0:
        menovalor = preço
        produtoMenor = produto
    if preço < menovalor:
        menovalor = preço
        produtoMenor = produto
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if saida == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total de compras foi de R$: {total:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtoMenor} e custou R$ {menovalor}')
