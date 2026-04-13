# Lados
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

# A sempre maior valor
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

# ver o tipo de triangulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    #por ângulos
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    #por lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")