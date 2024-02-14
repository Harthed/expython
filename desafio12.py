# programa que lê o preço de um produto e dá um desconto de 5%
print('Temos uma promoção! Digite o preço do produto que você deseja comprar abaixo e receba 5% de desconto!')
n = float(input('Digite o preço do produto: R$'))
print('Parabéns! Você ganhou 5% de desconto! \nValor original: R${} \nDesconto ganho: R${:.2f} \nNovo valor: R${:.2f}'.format(n, n * 0.05, n - (n * 0.05)))