from random import randint

v = 0
while True:
    player = int(input('Diga um valor: '))
    computer = randint(0, 10)
    total = player + computer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {player} e o computador {computer}. Total de {total} ', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')