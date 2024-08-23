#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E mostre NA TELA SUA TABUADA.

n = int(input('Digite um valor: '))

print ('A tabuada de {} e:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
