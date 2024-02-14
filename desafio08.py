# conversor de m para cm e mm
print('conversor simples de metros para centímetros e milímetros')
m = int(input('digite a distância em metros, sem incluir letras: '))
cm = m * 100
mm = m * 1000
print('a conversão de {} metros para centímetros resulta em {}cm \n a conversão de {} metros para milímetros resulta em {}mm'.format(m, cm, m, mm))