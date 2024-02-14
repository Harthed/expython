# programa que lê a velocidade de um carro, mostra uma multa se ele ultrapassar 80km/h que custa 7 reais por km acima do limite

print('Velocímetro. Limite: 80km/h')
v = int(input('Velocidade atual do veículo: '))
m = (v - 80) * 7
if v > 80:
    print('Limite de velocidade ultrapassado! Você recebeu uma multa de R${}!'.format(m))
else: 
    print('Tudo tranquilo, abaixo do limite.')
