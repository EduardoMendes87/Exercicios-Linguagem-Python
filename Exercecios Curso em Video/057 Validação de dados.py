'''
faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F 
caso esteja errado. peça a digitação novamente ate ter um valor correto.
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo= str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!!')
 