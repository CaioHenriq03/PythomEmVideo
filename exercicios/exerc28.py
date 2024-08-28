from random import randint
from time import sleep
computador = randint(0, 5) # FAZ SORTEIO NUMERO ALEATORIO
print("---==------==--- JOGO DA ADIVINHAÇÃO ---==------==---")
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print("---==------==--- JOGO DA ADIVINHAÇÃO ---==------==---")
jogador = int(input('Em que numero eu pensei? ')) # TENTAR ADIVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens! Voce acertou!')
else:
    print('O Computador Venceu!, ele pensou no numero {} e nao no {}'.format(computador, jogador))
