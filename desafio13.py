# programa que configura um aumento de 15% em um salário
print('Parabéns! Sendo o funcionário do mês por 3 meses seguidos, você merece um aumento!')
n = float(input('Qual era o seu salário original? R$'))

print('Salário original: R${} \nAumento: R${:.2f} \nNovo salário: R${:.2f} \nAgradecemos pelo seu esforço e esperamos mais contribuições!'.format(n, n * 0.15, n + (n * 0.15)))