# programa que calcula o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento. | à vista (dinheiro e cheque) - 10% desconto | à vista (cartão) = 5% desconto | 2x no cartão = preço normal | 3x ou mais no cartão = 20% juros
from time import sleep

print('-='*13)
print('Formas de pagamento. Escolha digitando \033[33m1\033[m, \033[33m2\033[m, \033[33m3\033[m ou \033[33m4\033[m.')
print('\033[33m1) À vista (dinheiro e cheque) = 10% desconto\n2) À vista (cartão) = 5% desconto\n3) Até 2x no cartão = preço normal\n4) 3x ou mais no cartão = 20% juros\033[m')
print('-='*13)

print(' ')
x = float(input('Insira o valor do produto: \033[32mR$\033[m'))
fp = int(input('Escolha uma forma de pagamento: '))
if fp == 4:
    p = int(input('Quantas vezes você deseja parcelar? '))
dc = x - (x * 0.10)
c = x - (x * 0.05)
c3 = x + (x * 0.20)

print(' ')
print('\033[35mCalculando...\033[m')
print(' ')
sleep(1)

if fp == 1:
    print('Valor: \033[32mR${:.2f}\033[m\nForma de pagamento escolhida: \033[33mÀ vista (dinheiro/cheque)\033[m\nDesconto: \033[36mR${:.2f}\033[m\nValor total: \033[32mR${:.2f}\033[m'.format(x, x * 0.10, dc))
elif fp == 2:
    print('Valor: \033[32mR${:.2f}\033[m\nForma de pagamento escolhida: \033[33mÀ vista (cartão)\033[m\nDesconto: \033[36mR${:.2f}\033[m\nNovo valor: \033[32mR${:.2f}\033[m'.format(x, x * 0.05, c))
elif fp == 3:
    print('Valor: \033[32mR${:.2f}\033[m\nForma de pagamento escolhida: \033[33m2x no cartão\033[m\nPrestações: \033[36m2\033[m\nValor das prestações: \033[32mR${:.2f}\033[m\nValor total: \033[32mR${:.2f}\033[m'.format(x, x / 2, x))
else:
    print('Valor: \033[32mR${:.2f}\033[m\nForma de pagamento escolhida: \033[33m{}x no cartão\033[m\nJuros: \033[31mR${:.2f}\033[m\nPrestações: \033[36m{}\033[m\nValor das prestações: \033[32mR${:.2f}\033[m\nValor total: \033[32mR${:.2f}\033[m'.format(x, p, x * 0.20, p, c3 / p, c3))
