# programa que lê um número inteiro e peça para o usuário escolher a base de conversão. 1 = binário | 2 = octal | 3 = hexadecimal
from time import sleep 

print('Conversor de números inteiros.')
x = int(input('Digite um número inteiro: '))
print('Conversão:')
print('1) Binário\n2) Octal\n3) Hexadecimal')
e = int(input('Faça sua escolha: '))

print(' ')
print('\033[35mCarregando...\033[m')
print(' ')
sleep(1)

if e == 1:
    print('{} em binário é {}'.format(x, bin(x)[2:]))
elif e == 2:
    print('{} em octal é {}'.format(x, oct(x)[2:]))
elif e == 3:
    print('{} em hexadecimal é {}'.format(x, hex(x)[2:]))
else:
    print('\033[41mOpção inválida.\033[m')