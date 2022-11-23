'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
EX:  Ana maria de souza
primeiro: Ana
ultimo: souza
'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
lista = nome.split()
print('Seu primeiro nome é ', lista[0])
print('Seu ultimo nome é ', lista[-1])
