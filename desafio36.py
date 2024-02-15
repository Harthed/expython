# programa de empréstimo bancário. pergunta o valor da casa, o salário e em quantos anos ele vai pagar, então calcula a prestação mensal. não pode exceder 30% do salário, ou será negado.
from time import sleep

print('--'* 15)
print('<Empréstimos bancários>')
print('--'* 15)
sleep(.8)

xc = float(input('- Insira o valor da casa: R$'))
xs = float(input('Insira o valor do seu salário: R$'))
xa = float(input('Em quantos anos o empréstimo pretende ser pago? '))
xp = xc / (xa * 12) 
m =  xs * 30 / 100

print('-='* 15)
print('\033[32mCalculando as prestações...\033[m')
print('-='* 15)
sleep(1.2)

if xp <= m:
       print('Valor das prestações mensais: R${:.2f}\nSeu salário: R${:.2f}\nValor do empréstimo: R${:.2f}\n\033[32mO empréstimo foi aceito.\033[m'.format(xp, xs, xc))
else:
    print('Valor das prestações mensais: R${:.2f}\nSeu salário: R${:.2f}\nValor do empréstimo: R${:.2f}\n\033[031mNão poderemos aceitar esse empréstimo.\033[m'.format(xp, xs, xc))
print('--'* 15)
