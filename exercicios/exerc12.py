preço = float(input('Qual e o preço do produto: R$: '))
novo = preço - (preço * 5 / 100)

print('O produto que custava R${:.2f}, na promocão com o desconto de 5% vai custar R${}.'.format(preço, novo))