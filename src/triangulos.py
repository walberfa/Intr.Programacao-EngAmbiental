"""Código usado para classificar um triangulo de acordo com os angulos inseridos pelo usuário."""

angulo_a = float(input("Digite o valor do angulo A: "))
angulo_b = float(input("Digite o valor do angulo B: "))
angulo_c = float(input("Digite o valor do angulo C: "))

soma = angulo_a + angulo_b + angulo_c
print("Soma dos angulos internos é igual a", soma)

if soma != 180:
    print("Os valores são inválidos para um triangulo")
elif angulo_a == 0 or angulo_b == 0 or angulo_c == 0:
    print("Um dos valores é igual a zero, logo não é um triangulo")
else:
    if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
        print("É um triangulo retangulo")
    elif angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
        print("É um triangulo obtusangulo")
    else:
        print("É um triangulo acutangulo")
