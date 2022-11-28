'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''


valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar: [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
print(f'A lista completa é {valores}')
for c in range(0, len(valores)): # for i, v in enumerate(valores): solução do guanabara
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
