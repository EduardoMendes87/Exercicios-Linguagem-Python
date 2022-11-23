'''
A confederação nacional de natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria, de 
acordo com a idade:
- ate 9 anos:MIRIM        - ate 25 anos: SENIOR
- ate 14 anos: INFANTIL   - Acima: MASTER
- ate 19 anos: JUNIOR
'''
from colorama import Fore, init
init(autoreset=True)
from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoatual - nascimento
print(Fore.YELLOW + f'O atleta tem {idade} anos.', )
if idade <= 9:
    print(Fore.GREEN + 'Classificação: MIRIM')
elif idade <= 14:
    print(Fore.RED + 'Classificação: INFANTIL')
elif idade <= 19:
    print(Fore.BLUE + 'Classificação: JUNIOR')
elif idade <= 25:
    print(Fore.MAGENTA + 'Classificação: SENIOR')
else:
    print(Fore.CYAN + 'Classificação: MASTER')
