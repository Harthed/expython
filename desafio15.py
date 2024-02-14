# programa que calcula o preço a pagar por um carro alugado. R$60 por dia e R$0,15 por km rodado
print('Este programa lhe auxiliará a calcular quanto deve ser pago pelo aluguel do carro.')
n1 = int(input('Há quantos dias o carro foi alugado? '))
n2 = float(input('Qual foi a distância percorrida pelo carro, em km? '))
d = n1 * 60
km = n2 * 0.15
print('Nossa conversão é: R$60,00 por dia e R$0,15 por km.')
print('Você alugou o carro há {} dias e percorreu {}km. \nValor diário: R${} \nValor distância: R${} \nValor total: R${}'.format(n1, n2, d, km, d + km))