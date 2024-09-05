from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
elif idade > 18:
            print('Voce deveria ter se alistado ha {} anos'.format(idade - 18))
            print('Seu alistamento foi em {}'.format(ano - (idade - 18)))
else:
    print('ERRO')
