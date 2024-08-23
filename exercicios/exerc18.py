import math
triangulo = float(input('Digite o Angulo que voce deseja: '))

seno = math.sin(math.radians(triangulo))
cos = math.cos(math.radians(triangulo))
tang = math.tan(math.radians(triangulo))

print('O valor do angulo de {} tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(triangulo, seno, cos, tang))