# programa que lê um numero aleatório entre 0 e 5 e pede pro usuário tentar adivinhar. deve escrever se o usuário venceu ou perdeu.
from random import randrange
from time import sleep

# print('-=-' * 30)
print('Vou escolher aleatóriamente um número de 0 a 5, tente adivinhar qual número eu escolhi!')
# print('-=-' * 30)
start = input('Aperte "Enter" para começar!')

# print('-=-' * 10)
print('Estou escolhendo um número...')
r = randrange(5)
sleep(2)
print('Escolhi!')
sleep(1)
x = int(input('Qual número você acha que eu escolhi? '))
sleep(.5)
if r == x:
    print('Você sabe ler mentes? Uau! Acertou em cheio!')
else:
    print('Errou hahaha! A resposta correta era {}, não {}!'.format(r, x))

# tentativa de fazer uma repetição abaixo xd

# rp = input('Quer jogar de novo? (y/n): ')
# s = 'y'
# if rp == s:
#     start
# else:
#     print('Tudo bem então! Até a próxima!')
