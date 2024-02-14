# programa que lê um nome e faz alterações: todo maiúsculo, minúsculo, contando todas as letras, contando a letras do primeiro nome

print('Olá! Esse programa é um leitor simples que mostra algumas informações sobre seu nome.')
n = input('Insira seu nome completo: ').strip()
l = len(n) - n.count(' ')
p = n.split()[0]

print('Nome inserido: {}\nNome totalmente maiúsculo: {}\nNome totalmente minúsculo: {}\nContagem de letras do nome: {}\nContagem de letras do primeiro nome: {}'.format(n, n.upper(), n.lower(), l, len(p)))