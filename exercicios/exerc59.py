somar = 0
multiplicar = 1
maior = 0
novosnumeros = 0
sair = 0
print('=-' * 20)
n1 = (int(input('Digite o primeiro valor: ')))
n2 = (int(input('Digite o segundo valor: ')))
print("=-" * 20)
print("""SUAS OPÇÕES:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA""")
opcao = int(input("Qual é a opção escolhida? "))

if opcao == 1:
    somar = n1 + n2
    print(f"A soma entre {n1} e {n2} vale {somar}")
elif opcao == 2:
    multiplicar = n1 * n2
    print(f"A multiplicação entre {n1} e {n2} vale {multiplicar}")
elif opcao == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print(f"Entre {n1} e {n2} o maior valor é {maior}")
elif opcao == 4:
    n1 = (int(input('Digite o primeiro valor: ')))
    n2 = (int(input('Digite o segundo valor: ')))
    print("=-" * 20)
    print("""SUAS OPÇÕES:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA""")
    opcao = int(input("Qual é a opção escolhida? "))
else:
    sair = 5