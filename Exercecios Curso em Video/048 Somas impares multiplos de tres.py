'''
Faça um programa que calcule a soma 
entre todos os numeros impares que são 
multiplos de 3 e que se encontra no intervalo de 1 ate 500
'''
cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {s}')
