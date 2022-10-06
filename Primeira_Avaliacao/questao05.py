#Quinta questão:

#Faça um programa para uma escola que, dadas três notas de um aluno e seu nome completo, exiba, no final, o nome do estudante, a média final e o seu conceito, observando que: a média final é calculada a partir da média aritmética simples das 3 notas; O conceito varia de acordo com a média.

nome = input("Olá! Por favor, digite seu nome completo: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Agora digite sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 95 and media <= 100:
  conceito = "A"
elif media >= 70 and media <= 94:
  conceito = "B"
elif media >= 50 and media <= 69:
  conceito = "C"
else:
  conceito = "D"


print(f"{nome} obteve conceito {conceito}\nAs notas fornecidas como entrada foram: {nota1:.2f}, {nota2:.2f} e {nota3:.2f} com Média final: {media:.2f}")