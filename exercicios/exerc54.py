from datetime import date

ano = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade'.format(totmenor))
