# programa que lê o ângulo inserido e  mostre o valor do seno, cosseno e da tangente 
from math import sin, cos, tan, radians
print('calculadora do seno, cosseno e tangente de um ângulo')
x = int(input('Insira o valor do ângulo: '))
rad = radians(x)
print('O valor do seno do ângulo {} é: {:.2f}'.format(x, sin(rad)))
print('O valor do cosseno do ângulo {} é: {:.2f}'.format(x, cos(rad)))
print('O valor da tangente do ângulo {} é: {:.2f}'.format(x, tan(rad)))
