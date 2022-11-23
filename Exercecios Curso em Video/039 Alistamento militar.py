'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar 
se é hora de se alistar ou se ja passou do tempo do alistamento.
seu programa tambem devera mostrar o tempo que falta ou que 
passou do prazo
'''

from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoatual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoatual}')
if idade < 18:    
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {18 + nascimento}!.')
elif idade > 18:    
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {nascimento + 18}!')
else:    
    print('Você tem que se alistar IMEDIATAMENTE!!')

