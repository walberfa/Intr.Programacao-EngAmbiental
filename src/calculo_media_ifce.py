def media_ifce(n1: float, n2: float):
    """Cálculo da média de acordo com o sistema de média ponderada do IFCE.

    Return: status do aluno baseado na média."""
    media = (n1 * 2 + n2 * 3) / 5
    print("Sua média é", media)

    if media >= 7:
        status = "aprovado"
    elif 3 <= media < 7:
        status = "em avaliação final"
    else:
        status = "reprovado"

    print(f"O aluno está {status}")
    return status
