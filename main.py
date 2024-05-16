from src.soma import soma
from src.calculo_media_ifce import media_ifce
from src.triangulos import verifica_se_valido, define_tipos
from src.verificacao_idades import verificacao_idade


def constroi_menu():
    print("MENU:\n1-soma\n2-calcula média ifce\n3-verifica triangulo\n4-verifica idade\n")


def main():
    menu = input("Escolha: ")
    if menu == "1":
        n1 = int(input("Digite o primeiro número da soma:"))
        n2 = int(input("Digite o segundo número da soma:"))
        soma(n1, n2)
    elif menu == "2":
        n1 = float(input("Digite a nota da N1:"))
        n2 = int(input("Digite a nota da N2:"))
        media_ifce(n1, n2)
    elif menu == "3":
        angulo_a = float(input("Digite o valor do angulo A: "))
        angulo_b = float(input("Digite o valor do angulo B: "))
        angulo_c = float(input("Digite o valor do angulo C: "))
        validez = verifica_se_valido(angulo_a, angulo_b, angulo_c)
        if validez:
            define_tipos(angulo_a, angulo_b, angulo_c)
    elif menu == "4":
        idade1 = int(input("Digite a primeira idade: "))
        idade2 = int(input("Digite a segunda idade: "))
        verificacao_idade(idade1, idade2)


if __name__ == "__main__":
    constroi_menu()
    main()
