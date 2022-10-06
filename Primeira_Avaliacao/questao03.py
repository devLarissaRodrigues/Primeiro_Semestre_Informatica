#Terceira questão:

#Em um sistema de supermercado, as maçãs custam R$1.50 cada, se forem compradas menos de uma dúzia; e custam R$ 1.10 cada, se o cliente comprar a partir de 12 maçãs. Escreva um algoritmo que leia a quantidade de maçãs compradas pelo cliente, calcule e escreva o custo total da compra. Exiba, na tela, o resultado do processamento com duas casas decimais, quando possível.

macas = int(input("Digite a quantidade de maças desejada: "))

if macas < 12:
  preco_final = 1.5 * macas
else:
  preco_final = macas * 1.1
  
print(f"Olá! Você comprou {macas} maças! O valor total a ser pago é de R$ {preco_final:.2f}")