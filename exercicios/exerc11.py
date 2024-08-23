n = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = n * a
tinta = area / 2
print('Sua parede tem {}m2 e vai precisar de {}l de tinta para pinta-la.'.format(area, tinta))