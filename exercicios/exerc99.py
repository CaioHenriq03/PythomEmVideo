from time import sleep

def maior(*num):
    cont = maior = 0
    result = []
    result.append('-=' * 30)
    result.append('Analisando os valores passados... ')
    for valor in num:
        result.append(f'{valor} ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    result.append(f'Foram informados {cont} valores ao todo.')
    result.append(f'O maior valor informado foi {maior}.')
    return '\n'.join(result)

output = maior(2, 9, 4, 5, 7, 1)
print(output)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()