'''
Desenvolva um programa que leia seis numeros inteiros e mostre a soma 
apenas daqueles que forem pares. se o valor for impar, desconsidere-o
'''
soma = 0
for c in range(1, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma de todos os números pares é {soma}')