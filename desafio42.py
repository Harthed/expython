# rograma que lê o comprimento de 3 retas e diz se elas podem formar um triângulo ou não (igual ao 35), e também mostra qual tipo de triângulo será formado. equilátero: todos os lados iguais | isósceles = dois lados iguais | escaleno = todos os lados diferentes
from time import sleep 

print('-='*15)
print('Analisador de triângulo.')
print('-='*15)
sleep(.5)

a = float(input('Insira o lado A: '))
b = float(input('Insira o lado B: '))
c = float(input('Insira o lado C: '))
tr = a + b > c and c + b > a and a + c > b

print('\033[35mCalculando...\033[m')
sleep(1)

if tr:
    print('\033[42mUm triângulo pode ser formado.\033[m')
if tr and a == b == c:
    print('O triângulo possui 3 lados iguais, então ele é \033[32mequilátero\033[m.')
elif tr and a == b or a == c or b == c:
    print('O triângulo possui 2 lados iguais, então ele é \033[33misósceles\033[m.')
elif tr and a != b != c:
    print('O triângulo possui os 3 lados diferentes, então ele é \033[31mescaleno\033[m.')
else:
    print('\033[41mUm triângulo não pode ser formado.\033[m')