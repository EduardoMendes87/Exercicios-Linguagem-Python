'''
 Desenvola uma logica que leia o pesso e a altura de uma pessoa
 calcule seu IMC e mostre se status, de acordo com a tabela abaixo:
 - Abaixo de 18.5: Abaixo do peso
 - Entre 18.5 e 25: Peso ideal
 -25 ate 30: Sobrepeso
 - 30 ate 40: obesidade
 - acima de 40: obesidade morbida
'''

from colorama import Fore, init
init(autoreset=True)
peso = float(input('Qual é o seu peso? (KG) '))
altura =  float(input('Qual sua altura? (m) '))
imc =  peso / (altura ** 2)
print(Fore.MAGENTA + f'O IMC dessa pesoa é de {imc:.2f}')
if imc < 18.5:
    print(Fore.YELLOW + 'Você está ABAIXO DO PESO ideal!')
elif imc < 25:
    print(Fore.GREEN + 'PARABENS você está no PESO IDEAL!')
elif imc < 30:
    print(Fore.MAGENTA + 'Você está com SOBREPESO!!')
elif imc < 40:
    print('Você esta com OBESIDADE!')
else:
    print(Fore.RED + 'Você está com OBSIDADE MORBIDA, CUIDADO')