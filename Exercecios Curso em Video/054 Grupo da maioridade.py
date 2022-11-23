'''
Crie um programa que çeia o ano de nascimentode sete pessoas. No
final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao de maior.
'''

from datetime import date
anoatual = date.today().year
print(anoatual)
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if anoatual - ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade!!')
print(f'E também tivemos {menor} pessoas de idade!!')