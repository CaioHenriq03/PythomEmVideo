import moeda

p = float(input("Digite o Preço: R$ "))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é  {moeda.dobro(p)}')
print(f'Aumentando em 10%, temos R$ {moeda.aumentar(p, 10)}')