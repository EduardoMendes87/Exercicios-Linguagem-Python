'''
crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maisculas e minusculas
- quantas letras ao todo (sem considerar os espaços)
- quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome completo: '))
print('Analizando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
espaços = nome.count(' ')
print(f'Seu nome tem ao todo {len(nome) - espaços} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
