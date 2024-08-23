import math
opost = float(input('Digite o Valor do Cateto Oposto: '))
cat = float(input('Digite o Valor do Cateto Adjacente: '))

hipotenusa = math.hypot(opost, cat)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))