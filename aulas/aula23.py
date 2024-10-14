try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):
    print("Infelizmente tivemos um problema com tipo de dado que você digitou :( ")
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print("O usúario preferiu não informar os dados! ")
except Exception as erro:
    print("O erro encontrado foi {erro._cause_} ")
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')