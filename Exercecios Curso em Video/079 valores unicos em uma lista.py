'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.
'''


lista = list()
num = 0
while True:
    num =(int(input('Digite um Valor: ')))
    if num in lista:
        print('VALOR DUPLICADO! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso....')
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
lista.sort()
print(f'A sua lista contém os seguintes valores {lista}')


