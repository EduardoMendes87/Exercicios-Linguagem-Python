'''
Melhore  o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 a 10,
so que agora o jogador vai tentar adivinhar ate acertar , mostrando no final
quantos palpites foram necessarios para vencer
'''


from random import randint
computador = randint(0, 10)
cont = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que vecê consegue adivinhar qual foi?''')
acertou = False
while not acertou:
    palpite = int(input('Qual é seu palpite: '))
    cont += 1    
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais... Tente mais uma vez.')
        elif palpite > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas. Parabéns!!!!')
