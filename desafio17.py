# programa que lê comprimento do cateto oposto e adjacente de um triângulo retângulo e calcula o comprimento da hipotenusa
from math import sqrt, pow

print('Calculadora da hipotenusa de um triângulo retângulo.')
a = float(input('Insira o valor de A, ou cateto adjacente: '))
b = float(input('Insira o valor de B, ou cateto oposto: '))
c = pow(a,2) + pow(b,2)
print('A = {} \nB = {} \nFórmula: A² + B² = C²\nValor da Hipotenusa(C) = {:.2f}'.format(a, b, sqrt(c)))