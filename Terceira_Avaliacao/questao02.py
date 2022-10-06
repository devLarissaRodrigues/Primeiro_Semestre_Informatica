#Faça um programa que receba um nome de um usuário como parâmetro e exiba a quantidade de letras que são vogais e a quantidade de consoantes. O programa deve utilizar uma função para verificar se uma letra é ou não uma vogal.

vogal = ['A','E','I','O','U']
vog = []

def obter_consoante():
  for indice in range(len(nome)):
    if nome[indice] in vogal:
      vog.append(nome[indice])
  consoante = len(nome) - len(vog)
  return consoante
 
nome = str(input("Digite seu nome: ")).upper()
cons = obter_consoante()
print(f"\nNo nome {nome} há {len(vog)} vogais e {cons} consoantes")

