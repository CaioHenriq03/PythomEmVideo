nome = str(input('Digite seu nome completo: ')).strip()

print('Muito Prazer em te conhecer {}!'.format(nome.split()[0] + ' ' + nome.split()[1]))

print('Seu primeiro nome é {}'.format(nome.split()[0]))

print("Seu primeiro nome é {}".format(nome.split()[-1]))
