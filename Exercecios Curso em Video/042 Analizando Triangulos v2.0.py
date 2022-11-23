'''
Refaça o desafio 035 dos triangulos, acrescentando o recurso de 
mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- isoceles: dois lados iguais
- escaleno: todos os lados diferentes
'''


from colorama import Fore, init
init(autoreset=True)
print(Fore.GREEN +'-=' * 20)
print(' ' * 7, Fore.RED + 'Analizador de Triâmgulos ')
print(Fore.GREEN + '-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triangulo', end='')
    if a == b == c:
        print(Fore.GREEN + ' EQUILATERO')
    elif a != b != c != a:
        print(Fore.CYAN + ' ESCALENO')
    else:
        print(Fore.BLUE + ' ISOSCELES')
else:
    print(Fore.RED + 'Os segmentos acima NÃO PODEM FORMAR trinagulo')
