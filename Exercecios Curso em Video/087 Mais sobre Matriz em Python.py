'''
Aprimore o desafio anterior, mostrando no final:
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

'''


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] =  int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos valores pares é {soma}')
somacol = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
maior = 0
for c in matriz[1]:
    if c > maior:
        maior = c
print(f'O maior valor da segunda linha é {maior}')
