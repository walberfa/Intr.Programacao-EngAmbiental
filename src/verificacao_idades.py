"""O código a seguir usa operadores lógicos para verificar se as idades inseridas pelo usuário
são de pessoas maiores de 18 anos."""


def verificacao_idade(idade1, idade2):
    # Lógica com o operador 'and'
    if idade1 >= 18 and idade2 >= 18:
        resposta = "Os dois são maiores de idade."
    else:
        resposta = "Pelo menos um dos dois não é maior de idade."
    # Lógica com o operador 'or'
    if idade1 >= 18 or idade2 >= 18:
        resposta = "Pelo menos um dos dois é maior de idade."
    else:
        resposta = "Os dois são menores de idade."

    print(resposta)
    return resposta
