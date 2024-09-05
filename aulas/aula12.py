nome = str(input('Qual seu nome? '))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome in ['Pedro', 'Maria', 'Paulo']:
    print('Seu nome e bem popular no Brasil')
elif nome in ['Ana', 'Cláudia', 'Jéssica', 'Juliana']:
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia {}!'.format(nome))