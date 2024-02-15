# programa que lê duas notas e calcula sua média, mostrando uma mensagem de acordo com a nota. abaixo de 5.0 = reprovado | entre 5.0 e 6.9 = recuperação | acima de 7.0 = aprovado
from time import sleep

print('-='*15)
print('\033[36mCalculadora de média escolar.\033[m')
print('--'*15)
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print(' ')
print('\033[35mCarregando...\033[m')
print(' ')
sleep(1)

print('Sua média foi: {}'.format(m))
if m < 5.0:
    print('\033[31mVocê foi reprovado.\033[m Estude mais da próxima vez.')
elif m > 7.0:
    print('\033[32mVocê foi aprovado. Parabéns!\033[m')
else:
    print('\033[33mVocê está de recuperação.\033[m')
print('--'*15)