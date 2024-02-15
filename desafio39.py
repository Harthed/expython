# programa que lê um ano de nascimento e diz se a pessoa vai se alistar um dia, se é o ano para essa pessoa se alistar ou se já passou da hora de se alistar. também mostra quanto tempo falta ou quanto passou do prazo.
from datetime import date
from time import sleep

print('Checador de idade para alistamento.')
x = int(input('Insira o ano do seu nascimento: '))
id = date.today().year - x
print('\033[35mCarregando...\033[m')
sleep(1)

if id > 18:
    print('Você devia ter se alistado há {} anos.'.format(id - 18))
elif id < 18:
    print('Você deverá se alistar em {} anos.'.format(18 - id))
else:
    print('Você deve se alistar nesse ano.')