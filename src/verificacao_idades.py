"""O código a seguir usa operadores lógicos para verificar se as idades inseridas pelo usuário
são de pessoas maiores de 18 anos."""

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

# Lógica com o operador 'and'
if idade1 >= 18 and idade2 >= 18:
    print("Os dois são maiores de idade.")
else:
    print("Pelo menos um dos dois não é maior de idade.")
# Lógica com o operador 'or'
if idade1 >= 18 or idade2 >= 18:
    print("Pelo menos um dos dois é maior de idade.")
else:
    print("Os dois são menores de idade")
