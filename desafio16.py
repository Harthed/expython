# programa que lê número real e mostre sua versão inteira
from math import floor

print('Conversor de número real para número inteiro.')
r = float(input('Digite um número real. Ex: 6.127 = '))
print('O número real {} tem sua contraparte inteira {}.'.format(r, floor(r)))