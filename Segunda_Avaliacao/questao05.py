# Faça um programa para uma escola que, dadas três notas obrigatórias de um aluno e seu nome completo, exiba, no final, o nome do estudante, notas, a média final e o seu conceito. 

aluno = input("Digite seu nome completo: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

lista_notas = [nota1, nota2, nota3]
media = sum(lista_notas)/len(lista_notas)

if media >= 80:
  conceito = 'A'
elif media >= 50 and media < 80:
  conceito = 'B'
else:
  conceito = 'C'

lista_final = [aluno, nota1, nota2, nota3, media, conceito]

print(f"\n{lista_final}")
print(f"{aluno} obteve conceito {conceito}\nAs 3 notas fornecidas como entrada foram: {lista_notas} com Média final: {media:.2f}")
