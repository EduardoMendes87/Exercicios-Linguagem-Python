'''
Crie um programa que leia dois valores e mostre um menu como o ao lado na tela
seu programa devera realizar a operação solicitada em cada caso
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
'''

from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opçao = int(input('>>>>> Qual é sua opção? '))
    if opçao == 1:
        soma = num1 + num2
        print(f'Asoma entre {num1} + {num2} é {soma}')
    elif opçao == 2:
        multiplicar = num1 * num2
        print(f'O resultado de {num1} x {num2} é {multiplicar}')
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opçao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Você digitou uma opçâo inválida... Tente novamente!')
    print('=-=' * 10)
sleep(1)
print('Fim do programa! Volte sempre!')

