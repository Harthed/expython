# programa que lê 3 números e mostra qual é o maior e qual é o menor

print('Identificador de número maior e menor. Insira três números.')
x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))
z = int(input('Insira o terceiro número: '))
ma = x
me = x

# maior
if y > ma:
    ma = y
if z > ma:
    ma = z

# menor
if y < me:
    me = y
if z < me:
    me = z

print('Maior: {}\nMenor: {}'.format(ma, me))
