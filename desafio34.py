# programa que dá aumento no salário. se for menor ou igual a 1250, 15% de aumento. se for maior, 10%

print('Calculador de aumento de salário.')
x = float(input('Valor do salário: R$'))
if x <= 1250:
    print('Salário anterior: R${}\nValor do aumento: R${}\nNovo salário: R${}'.format(x, x * 0.15, x + (x * 0.15)))
else:
    print('Salário anterior: R${}\nValor do aumento: R${}\nNovo salário: R${}'.format(x, x * 0.10, x + (x * 0.10)))
