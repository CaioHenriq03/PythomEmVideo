salario = float(input('Qual o valor do salário do Funcionario? '))

aumento = (salario * 15/100) + salario

print('um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))