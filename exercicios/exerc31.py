viagem = float(input('Qual a distância da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km.'.format(viagem))
preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preco))