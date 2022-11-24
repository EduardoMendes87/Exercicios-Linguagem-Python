'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Fortaleza

'''

tabela = ('Palmeiras', 'internacional', 'Fluminense', 'Corinthians',
        'Flamengo', 'Atletico-PR', 'Atletico-MG', 'Fortaleza',
        'São Paulo', 'America-MG', 'Botafogo', 'Santos', 'Goias',
        'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atletico-GO',
        'Avaí', 'Juventude')

print('-='*18)
print(f'Lista de times do Brasileirão 2022: {tabela}')
print('-='*18)
print(f'Os 5 primeiro são: {tabela[:5]}')
print('-='*18)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*18)
print(f'Times na ordem alfabética: {sorted(tabela)}')
print('-='*18)
print(f'O Fortaleza está na {tabela.index("Fortaleza") + 1}° posição')
print('-='*18)
