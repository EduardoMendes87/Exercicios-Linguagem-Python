# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida}m correspode a {cm:.0f}cm e {mm:.0f}mm')