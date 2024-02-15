# programa de pedra, papel e tesoura
from time import sleep 
from random import randint

print('-='*15)
print('Vamos jogar Jokenpô!')
print('Digite 0 para pedra!\nDigite 1 para papel!\nDigite 2 para tesoura!')
print('-='*15)
sleep(.8)

ul = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Digite um número baseado na lista acima: '))

print('JO')
sleep(.5)
print('KEN')
sleep(.6)
print('PO!')
sleep(.8)
print('-=' * 11)
print('Eu joguei {}\nVocê jogou {}'.format(ul[computador], ul[jogador]))
print('-=' * 11)

pedra = 0
papel = 1
tesoura = 2
if computador == pedra and jogador == tesoura or computador == papel and jogador == pedra or computador == tesoura and jogador == papel: #Todas as situações em que o computador ganha
    print('Eu venci hahahaha!')
elif computador == jogador:
    print('Eita! Empatamos!')
elif computador == pedra and jogador == papel or computador == papel and jogador == tesoura or computador == tesoura and jogador == pedra:
    print('Uau, você venceu!')