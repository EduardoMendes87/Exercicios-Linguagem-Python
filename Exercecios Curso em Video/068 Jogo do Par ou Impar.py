'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''

from random import randint
print('=-' * 13)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 13)
cont = 0
while True: 
    computador = randint(0, 10)   
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou impar? [P/I] ')).upper()     
    soma = valor + computador   
    if soma % 2 == 0:
        resultadoPar = 'PAR'
    else:
        resultadoPar = 'IMPAR'
    lista = list(resultadoPar)    
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} deu {resultadoPar} ')
    print('-' * 10)
    if escolha == lista[0]:
        print('''Você venceu
        Vamos jogar novamente..''')
        cont += 1
    else:
        print(f'GAME OVER. Você venceu {cont} vezes.')       
        break
print('=-' * 10)



# Codigo do Guanabara
'''
from random import randit
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo =  str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')   
'''
