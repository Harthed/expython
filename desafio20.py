# programa que escolhe aleatóriamente a ordem que os nomes serão mostrados
from random import shuffle

print('Vou escolher aleatóriamente a ordem quem vocês apresentarão o trabalho!')
lista = ['Ana', 'Pedro', 'Gabriel', 'Duda']
shuffle(lista)
print('A ordem sorteada foi:')
print(lista)