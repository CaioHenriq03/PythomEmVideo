a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('E um número? {}'.format(a.isnumeric()))
print('E alfabético? {}'.format(a.isalpha()))
print('E alfanúmerico? {}'.format(a.isalnum()))
print('Esta em maiúsculas? {}'.format(a.isupper()))
print('Esta em minúsculas? {}'.format(a.islower()))
print('Esta capitalizado? {}'.format(a.istitle()))