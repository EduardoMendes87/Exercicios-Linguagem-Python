'''
Faça um programa que leia o pesso de cinco pessoas
No final mostre qual foi o maior e o menor peso lidos.
'''
maior: 0
menor: 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')
