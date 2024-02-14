# programa que lê um nome completo e transcreve o primeiro e o último nome da pessoa

print('Separador de primeiro e último nome.')
n = input('Insira seu nome: ')

print('Primeiro nome: {}\nÚltimo nome: {}'.format(n.split()[0], n.split()[-1])) 