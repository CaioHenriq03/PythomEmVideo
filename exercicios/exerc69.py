tot18 = tothomens = totmulher20 = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
        if sexo == 'M':
            tothomens += 1
        if sexo == 'F' and idade < 20:
            totmulher20 += 1
resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
if resp == 'N':
    break
print('Total de pessoas com mais de 18 anos: {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(tothomens))
print('E temos {} mulheres com menos de 20 anos'.format(totmulher20))
