# programa que lê o nome de uma cidade e diz se ela começa com "Santo" ou não

print('Leitor de nome de cidade: Santo').strip()
n = input('Insira o nome de uma cidade: ')
s = 'Santo' in n.split()[0]

print('Possui "Santo" no nome: {}'.format(s))