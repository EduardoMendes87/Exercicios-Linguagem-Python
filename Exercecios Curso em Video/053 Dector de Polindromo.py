'''
Crie un programa que leia uma frase se ela é 
um polindromo, desconsiderando os espaços
'''

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
fraseI = frase[::-1]
print(f'O inverso de {frase} é {fraseI}')
if frase == fraseI:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!!!')
