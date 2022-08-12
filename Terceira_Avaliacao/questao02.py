#Faça um programa que receba um nome de um usuário como parâmetro e exiba a quantidade de letras que são vogais e a quantidade de consoantes. O programa deve utilizar uma função para verificar se uma letra é ou não uma vogal.

vogal = ['A','E','I','O','U']
vog = []

def obter_consoante():
  for v in range(len(nome)):
    if nome[v] in vogal:
      vog.append(nome[v])
  consoante = len(nome) - len(vog)
  return consoante

  
def saida():
  print(f"Sua entrada foi {nome}")
  print(f"Vogais: {len(vog)} Letras")
  print(f"Consoantes: {cons} Letras")

nome = str(input("Digite seu nome: ")).upper()

cons = obter_consoante()
saida()

