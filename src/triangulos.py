"""Código usado para classificar um triangulo de acordo com os angulos inseridos pelo usuário."""


def verifica_se_valido(a, b, c):
    soma = a + b + c
    if soma != 180:
        print("Os valores são inválidos para um triangulo")
        return False
    elif a == 0 or b == 0 or c == 0:
        print("Um dos valores é igual a zero, logo não é um triangulo")
        return False
    else:
        return True


def define_tipos(angulo_a, angulo_b, angulo_c):
    if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
        resultado = "retangulo"
    elif angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
        resultado = "obtusangulo"
    else:
        resultado = "acutangulo"
    print(f'É um triangulo {resultado}.')
    return resultado
