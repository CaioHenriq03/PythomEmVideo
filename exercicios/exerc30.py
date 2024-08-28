n = int(input('Digite um número inteiro: '))
resultado = n % 2 == 0
if resultado == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))

