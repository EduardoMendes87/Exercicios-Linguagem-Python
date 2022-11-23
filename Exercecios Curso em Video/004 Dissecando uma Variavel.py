# faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela!

a = input('Digite algo : ')
print('O tipo primitivo é ', type(a))
print('So tem espaços? ', a.isspace())
print('E um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiscula? ', a.isupper())
print('Está em minuscula? ', a.islower())
print('Está capitalizada? ', a.istitle())
        