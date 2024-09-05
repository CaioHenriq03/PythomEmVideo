tab = int(input('Quer ver a tabuada de qual valor? '))

print('-' * 15)
for c in range(1, 11):
    print('{} x {} = {}'.format(tab, c, tab * c))