cont = ('zero', 'um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
num = int(input('digite um numero entre 0 e 20: '))

if 0 <= num <= 20:
    print(f'Você digitou o número {cont[num]}'.upper())
else:
    print('Numero fora do intervalo')

