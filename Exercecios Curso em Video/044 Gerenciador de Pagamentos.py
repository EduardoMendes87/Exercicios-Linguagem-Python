'''
elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- avista dinheiro ou cheque: 10% de desconto
- a vista no cartao: 5% desconto
- em ate 2x no cartão : preço normal
- 3x ou mais no cartão 20% de juros
'''

print('='*10, 'LOJAS EMENDES', '='*10)
preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    novopreço = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${novopreço} no final.')
elif opção == 2:
    novopreço = preço - (preço * 5 / 100)
    print(f'sua compra de R${preço:.2f} vai custar R${novopreço} no final.')
elif opção == 3:
    parcela = preço / 2
    print(f'Sua compra de R${preço:.2f} será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opção == 4:
    novopreço = preço + (preço * 20 / 100)
    quantidade = int(input('Quantas parcelas? '))
    parcela = novopreço / quantidade
    print(f'Sua compra será parcelada em {quantidade}x de R${parcela:.2f} COM JUROS')
    print(f'Sua Compra de R${preço} vai custar R${novopreço} no final.')
else:
    print('Opção inválida. Tente novamente!')
    