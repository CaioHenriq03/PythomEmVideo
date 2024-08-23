km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
pago = (dias * 60) + (km * 0.15)

print('O Carro percorreu {}km e ficou alugado por {} dias, totalizando um custo de {} Reais.'.format(km, dias,pago))