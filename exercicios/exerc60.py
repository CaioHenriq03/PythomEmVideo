n1 = int(input('Calculando o Fatorial de um numero: '))

fatorial = 1
for c in range(n1, 0, -1):
    fatorial *= c
print('O Fatorial de {} e {}.'.format(n1, fatorial))