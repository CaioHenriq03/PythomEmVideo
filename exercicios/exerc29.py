vel = int(input('Qual a velocidade do carro? '))
multa = (vel - 80) * 7

if vel > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    print('Você deve pagar uma multa de {} reais'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')