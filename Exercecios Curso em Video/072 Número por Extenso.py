'''
Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre
0 e 20) e mostrá-lo por extenso.
'''

tupla = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE',
'VINTE')


while True:        
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <=20: # if 0<= num <=20: guanabara usou esse codigo pra validar a entrada
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {tupla[num]}')
