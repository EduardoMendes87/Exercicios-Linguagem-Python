'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre
a idade media do grupo
qual o nome do homem mais velho
quantas mulheres tem menos de 20 anos
'''
idademaisvelho = 0
nomemaisvelho = ''
idadetotal = 0
contmulher = 0
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    idadetotal += idade
    if sexo == 'M':
        if idade > idademaisvelho:
            idademaisvelho = idade
            nomemaisvelho = nome
    elif sexo == 'F':
        if idade < 20:
            contmulher += 1
media = idadetotal / 4
print(f'A média de idade do grupo é de {media} anos!')
print(f'O homem mais velho tem {idademaisvelho} e se chama {nomemaisvelho}!')
print(f'Ao todo são {contmulher} mulheres com mendos de 20 anos!')