'''
Faça um programa que leia uma frase pelo teclado e mostre:
- quantas veses aparece a letra "A"
- em que posição aparece a primeira vez.
- em que posição aparece a ultima vez
'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece', frase.count('A'), 'vezes na frase.')
print('A primeira letra A aparececeu na posição', frase.find('A') + 1)
print('A ultima letra A apareceu na posição', frase.rfind('A') + 1)
