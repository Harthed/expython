# programa simples que mostra tabuada de um número inteiro
print('tabuadas')
n = int(input('digite um número: '))
print('a tabuada de {} é:'.format(n))

for count in range(10):
    print('{} x {} = {}'.format(n, count + 1, n * (count + 1)))