n1 = int(input('Digite um número [999 para parar]: '))
soma = 0
cont = 0
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma entre eles foi {}.'.format(cont, soma))