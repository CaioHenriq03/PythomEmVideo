print("---==------==------==------==---")
print("         LOJAS DO CAIO       ")
print("---==------==------==------==---")
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} parcelas de R${:.2f} COM JUROS'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    total = 0
    print('Opção inválida! Tente novamente.')