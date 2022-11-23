'''
Crieu um programa que leia varios números inteiros pelo teclado. O programa só vai para
quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitador 
e qual foi a soma entre eles(desconsiderndo o flag)
'''

condição = False
cont = soma = 0
while not condição:
    n = int(input('Digite um numero [999] para parar: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        condição = True
print(f'Você digitou {cont} números e a soma entres eles foi {soma}.')