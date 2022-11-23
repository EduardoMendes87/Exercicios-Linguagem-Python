'''
Escreva um programa que leia a velocidade de um carro.
se ele ultrapaçar 80km/h, mostre que ele foi multado.
a multa vai custar R$ 7.00 por cada acima do limite.
'''
from colorama import Fore, init
init(autoreset=True)
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(Fore.RED +'MULTADO! Voçê execedeu o limite de velociade que é 80KM/H')
    print(Fore.RED + 'Você deve pagar uma multa de' + Fore.YELLOW + f' R${multa:.2f}!')
print(Fore.GREEN + 'Tenha um bom dia! Dirija com segurança')
