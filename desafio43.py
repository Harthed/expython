# programa que lê a altura e o peso de uma pessoa, calcula seu imc e mostra se a pessoa está abaixo do peso = menos de 18.5 | no peso ideal = entre 18.5 e 25 | sobrepeso = 25 a 30 | obesidade = 30 a 40 | obesidade mórbida = acima de 40
from time import sleep
from math import pow

print('-='*10)
print('Calculador de IMC.')
print('-='*10)
sleep(.5)

h = float(input('Insira sua altura em metros: '))
p = float(input('Insira seu peso em Kg: '))
imc = p / (pow(h, 2))

print(' ')
print('\033[35mCalculando...\033[m')
print(' ')
sleep(1)

print('Altura inserida: {:.2f}m\nPeso inserido: {:.2f}kg\nIMC: {:.1f}'.format(h, p, imc))
if imc < 18.5:
    print('\033[34mVocê está abaixo do peso.\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif imc > 25 and imc < 30:
    print('\033[33mVocê está com sobrepeso.\033[m')
elif imc > 30 and imc < 40:
    print('\033[35mVocê está com obesidade.\033[m')
else:
    print('\033[41mVocê possui obesidade mórbida e deve urgentemente perder peso.\033[m')
print('---'*20)