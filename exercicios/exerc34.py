salario = float(input('Qual é o salário do funcionario? R$ '))

if salario >= 1250.00:
    novo = (salario * 10 / 100) + salario
    print('Um funcionario que ganhava R${:.2f}, com 10% de aumento, passa a receber R${:.2f}'.format(salario, novo))
else:
    novo = (salario * 15 / 100) + salario
    print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
