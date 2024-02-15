# programa que lê dois números inteiros e os compara, mostrando uma mensagem dizendo se um dos dois é maior ou se ambos são iguais.
from time import sleep

print('--'* 15)
print('Identificador numeral.')
print('--'* 15)

x1 = int(input('Digite um número: '))
x2 = int(input('Digite mais um número: '))
print('\033[35mCarregando...\033[m')
sleep(1)

print('\033[33mNúmeros inseridos:\033[m {} e {}'.format(x1, x2))
if x1 > x2:
    print('O primeiro valor ({}) é maior que o segundo ({}).'.format(x1, x2))
elif x2 > x1:
    print('O segundo valor ({}) é maior que o primeiro ({}).'.format(x2, x1))
else:
   print('\033[34mAmbos os números são iguais.\033[m')