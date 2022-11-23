'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado
for negativo.
'''

while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('-' * 35)
    for c in range(1, 11):        
        print(f'{tab} x {c} = {c * tab}')
    print('-' * 35)    
print('PROGRAMA DE TABUADA ENCERRADA. Volte sempre!')
