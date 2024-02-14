# programa que escolhe um nome aleatóriamente entre os que foram dados
from random import choice

print('Vou escolher o nome de um de vocês aleatóriamente pra vir me ajudar!')
lista = ['Ana', 'Pedro', 'Gabriel', 'Duda']
print('Nome sorteado: {}'.format(choice(lista)))