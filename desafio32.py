# programa que lê um ano qualquer e mostra se ele é bissexto
from datetime import date

print('Leitor de ano bissexto.')
x = int(input('Insira um ano. Digite 0 se quiser checar o ano atual: '))

if x == 0:
    x = date.today().year

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('{} é um ano bissexto.'.format(x))
else:
    print('{} não é um ano bissexto.'.format(x))
    