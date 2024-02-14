# programa que calcula a área de uma parede e mostra a quantidade de tinta necessária
print('Olá, pintor! Este programa irá te ajudar a calcular quantos litros de tinta você precisará para pintar sua parede!')
b = float(input('Digite a largura da parede (em metros): '))
h = float(input('Digite a altura da parede (em metros): '))
A = b * h
print('A área da parede é de {}m², então serão necessários {} litros de tinta.'.format(A, A / 2))