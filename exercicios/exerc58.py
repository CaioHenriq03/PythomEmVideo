from random import randint
from time import sleep

computador = randint(0, 10)  # FAZ SORTEIO NUMERO ALEATORIO
print("---==------==--- JOGO DA ADIVINHAÇÃO ---==------==---")
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar...")
print("---==------==--- JOGO DA ADIVINHAÇÃO ---==------==---")
print("PROCESSANDO...")
acertou = False
palpite = 0  # Initialize palpite
while not acertou:
    jogador = int(input("Qual seu palpite? "))  # TENTAR ADIVINHAR
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print("Parabens! Voce acertou com um total de {} tentativas!".format(palpite))