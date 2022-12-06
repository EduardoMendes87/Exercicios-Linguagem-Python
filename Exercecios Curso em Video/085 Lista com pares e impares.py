'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.
'''


num = []
pares = []
impares = []


for c in range(0, 7):
    num.append(int(input(f'Digite o {c + 1}° valor:  ')))
for p in num:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print('-='*25)
pares.sort()
print(f'Os valores pares digitados foram: {pares}')
impares.sort()
print(f'Os valores ímpares digitados foram: {impares}')


'''
Solução correta, errei porque tinha que estar tudo em uma lista só e eu fiz separando em 3 listas

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}°. Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

'''