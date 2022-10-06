#Primeira questão

#Escreva um programa que possa ler um número inteiro entre 1 e 12 e, assumindo que esse valor representa um determinado mês do ano, imprimir o nome do mês por extenso. O programa deve verificar se uma entrada inválida foi digitada pelo usuário do programa (por exemplo, -5 ou 100). Neste caso, o programa deve exibir na tela apenas uma mensagem de erro.

num = int(input("Olá! Digite um número inteiro entre 1 e 12: "))

if num == 1:
  msg = "janeiro"
elif num == 2:
  msg = "fevereio"
elif num == 3:
  msg = "março"
elif num == 4:
  msg = "abril"
elif num == 5:
  msg = "maio"
elif num == 6:
  msg = "junho"
elif num == 7:
  msg = "julho"
elif num == 8:
  msg = "agosto"
elif num == 9:
  msg = "setembro"
elif num == 10:
  msg = "outubro"
elif num == 11:
  msg = "novembro"
elif num == 12:
  msg = "dezembro"
else:
  msg = "inválido. ERRO!"

print(f"Olá! O mês referente ao que foi digitado é: {msg}")