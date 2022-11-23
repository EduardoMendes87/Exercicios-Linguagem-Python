# faça um aalgoritimo que leia o preço de um produto e mostre se novo preço, com 5% de desconto

preço = float(input('Qual é o preço do produto: R$'))
desconto = preço / 100 * 95
# desconto = preço - (preço * 5 / 100) exemplo da aula e calculo de forma matematica.

print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai custar R${desconto:.2f}.')