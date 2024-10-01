from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f"Contagem de {i} até {f} de {p} em {p}")

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")
contador(0, 100, 10)
contador (10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)