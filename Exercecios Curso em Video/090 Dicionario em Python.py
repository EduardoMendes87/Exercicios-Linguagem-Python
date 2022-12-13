'''
Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''


alunos = {}

alunos['aluno'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["aluno"]} '))
print('-='*30)
print(f'     - Nome é igual a {alunos["aluno"]}')
print(f'     - Média é igual a {alunos["Média"]}')
if alunos['Média'] >= 7:
    print(f'     - Situação é igual a Aprovado!!')
else:
    print(f'     - Situação é igual a Reprovado!!')
print('-='*30)
