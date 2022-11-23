# faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua area e a quantidade de tinta necessaria para pinta - la,
# sabendo que cada litro de tinta, pinta uma area de 2m

largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede: '))

area = largura * altura
print(f'Sua parede tema dimenção de {largura} x {altura} e sua area é de {area}m²')

tinta = area / 2
print(f'Para pintar essa parede, voce precisa de {tinta}l de tinta.')
