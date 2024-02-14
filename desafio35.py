# programa que lê o comprimento de 3 retas e diz se elas podem formar um triângulo ou não
from time import sleep
print('-='*15)
print('Analisador de triângulo.')
print('-='*15)
sleep(.5)

a = float(input('Insira o lado A: '))
b = float(input('Insira o lado B: '))
c = float(input('Insira o lado C: '))
print('Calculando...')
sleep(1)

if a + b > c and c + b > a and a + c > b:
    print('Um triângulo pode ser formado.')
else:
    print('Um triângulo não pode ser formado.')
    