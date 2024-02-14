# programa que lê uma frase e mostra quantas vezes a letra "A" aparece, em que posição ela aparece pela primeira vez e em que posição aparece na última vez

print('Leitor de frase: letra A')
f = input('Digite uma frase: ').strip().upper()
c = f.count('A')
p = f.find('A') + 1
u = f.rfind('A') + 1

print('Frase inserida: {}\nQuantidade de vezes que a letra A aparece: {}\nPosição da primeira letra A: {}\nPosição da última letra A: {}'.format(f, c, p, u))