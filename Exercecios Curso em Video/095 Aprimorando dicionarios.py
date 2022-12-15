'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''



time = list()
tot = 0
gols = []
dados = dict()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    gols.clear()
    for c in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na partida {c}? ')))
        tot += gols[c-1]   # jogador['total] =sum(gols) soma automatico 
    dados['gols'] = gols[:]
    dados['Total'] = tot
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*30)
print('<<< VOLTE SEMPRE >>>')
