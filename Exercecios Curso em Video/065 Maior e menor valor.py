'''
Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a media entre todos os valores e qual foi o maior 
e o menor valor lido. o programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
'''

c = 'S'
soma = cont = maior = menor = 0
while c != 'N':
    n = int(input('Digite um número: '))    
    soma += n
    cont += 1 
    if cont == 1 :
        maior = menor = n
    else:   
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}'
)
