'''
Crie um progrma que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acordo com a media atingida:
- media abaixo de 5.0: REPROVADO
- media entre 5.0 e 6.9: RECUPERÇÃO
- media 7.0 ou superior: APROVADO
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1F} e {nota2:.1F}, a média do aluno é {media:.1F}')
if media >= 7.0:
    print('O aluno está APROVADO.')
elif media < 5.0:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está em RECUPERÇÃO.')