listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para posicao {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor}', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')