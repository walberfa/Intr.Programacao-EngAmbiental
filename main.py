from src.soma import soma
from src.calculo_media_ifce import media_ifce


def main():
    menu = input("MENU:\n1-soma\n2-média_ifce\nEscolha: ")
    if menu == "1":
        n1 = int(input("Digite o primeiro número da soma:"))
        n2 = int(input("Digite o segundo número da soma:"))
        soma(n1, n2)
    elif menu == "2":
        n1 = float(input("Digite a nota da N1:"))
        n2 = int(input("Digite a nota da N2:"))
        media_ifce(n1, n2)


if __name__ == "__main__":
    main()
