times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro',
        'Sao Paulo', 'Bahia', 'Vasco', 'Atletico-MG', 'Internacional',
        'RB Bragantino', 'Athetico', 'Juventude', 'Criciuma', 'Gremio',
        'Fluminense', 'Corinthias', 'Vitoria', 'Cuiaba', 'Atletico GO'
        )
print('-=' * 15)
print('Lista de times do Brasileirão: {}'.format(times))
print("-=" * 15)
print('Os 5 Primeiros sao {}'.format(times[:5]))
print("-=" * 15)
print('Os 4 ultimos sao {}'.format(times[-4:]))
print("-=" * 15)
print('Times em ordem alfabetica: {}'.format(sorted(times)))
print("-=" * 15)
print('O Vasco esta na {} posicao'.format(times.index('Vasco')+1))