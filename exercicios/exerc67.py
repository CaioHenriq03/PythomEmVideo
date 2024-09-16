while True:
    print('-+-' * 20)
    tab = int(input("Quer ver a tabuada de qual valor? "))
    print('-+-' * 20)
    if tab < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(tab, c, tab * c))
print('Programa tabuada encerrado. Volte sempre!')