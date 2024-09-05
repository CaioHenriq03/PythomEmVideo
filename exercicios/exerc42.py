print("---==------==------==------==---")
print("ANALISADOR DE TRIANGULOS")
print("---==------==------==------==---")

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR UM TRIANGULO")
    if r1 == r2 == r3:
        print("TRIANGULO EQUILATERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("TRIANGULO ISOSCELES")
    else:
        print("TRIANGULO ESCALENO")
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO")