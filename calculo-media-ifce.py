# Cálculo da média e print na tela do status de aprovação, de acordo com o sistema de média ponderada do IFCE

n1 = int(input("Insira a nota da N1:"))
n2 = int(input("Insira a nota da N2:"))

media = ((n1*2 + n2*3) / 5)
print("Sua média é", media)

if media >= 7:
  print("O aluno está aprovado!")
elif media >=3 and media <7:
  print("O aluno deverá fazer a avaliação final.")
else:
  print("O aluno está reprovado!")
