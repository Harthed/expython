# programa que lê um número de 0 a 9999 e mostra suas unidades (unidade, dezena, centena, milhar)

print('Leitor simples de unidade')
x = int(input('Insira um número de 0 a 9999: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))