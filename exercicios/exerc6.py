#CRIE ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro do seu número e {}, o triplo e {}, e a raiz quadrada e {:.2f}'.format(d, t, r))
