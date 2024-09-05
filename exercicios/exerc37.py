n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opcão: '))

if opcao == 1:
    print('{} convertido para BINÁRIO vale {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL vale {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL vale {}.'.format(n, hex(n)[2:]))
else:
    print('Opcão inválida! Tente novamente.')