valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
anos = int(input('Em quantos anos vai pagar? '))
prestacao = valor / (anos * 12)
minima = prestacao / 100 * 30

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestacao))

if prestacao <= minima:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

