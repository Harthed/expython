# programa que pergunta distância da viagem em km e calcula o preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas que 200km

print('Calculador de preço de viagem.')
x = int(input('Insira a distância da viagem: '))
if x <= 200:
    print('O preço a pagar será de R${:.2f}'.format(x * 0.50))
else:
    print('O preço a pagar será de R${:.2f}'.format(x * 0.45))
