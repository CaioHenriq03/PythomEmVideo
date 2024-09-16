palavras = ('aprender', 'programar', 'linguagem',
            'falar', 'dizer', 'fazer', 'mexer',
            'curso', 'estudar', 'baralho','jogar',
            'assistir','futoro', 'futebol','flamengo',
            'titulo', 'soltar','pipa', 'lazer','brincar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')