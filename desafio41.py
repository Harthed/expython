#  programa que lê o ano de nascimento de um atleta e diga sua categoria. até 9 anos = mirim | até 14 = infantil | até 19 = júnior | até 20 = sênior | acima de 20 = master
from time import sleep
from datetime import date

print('--'*15)
print('Identificador de categoria.')
print('--'*15)
x = int(input('Insira seu ano de nascimento: '))
id = date.today().year - x

print(' ')
print('\033[35mCarregando...\033[m')
print(' ')
sleep(1)

print('Idade: {} anos'.format(id))
if id <= 9:
    print('Sua categoria é: \033[36mMirim\033[m.')
elif id > 9 and id <= 14:
    print('Sua categoria é: \033[34mInfantil\033[m.')
elif id > 14 and id <= 19:
    print('Sua categoria é: \033[33mJúnior\033[m.')
elif id > 19 and id < 21:
    print('Sua categoria é: \033[32mSênior\033[m.')
else:
    print('Sua categoria é: \033[31mMaster\033[m.')
print('--'*15)
