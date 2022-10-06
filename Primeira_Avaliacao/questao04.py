#Quarta questão:

#Escreva um programa para uma loja capaz de calcular o valor final da compra para um cliente. O programa deve receber como entrada: a) o valor da compra, e b) a quantidade de parcelas desejada. Importante! se o número de parcelas for igual a “1” (ou seja, pagamento à vista), o programa deverá aplicar um desconto de 10% sobre o valor inicial da compra e exibir apenas o valor final calculado. Porém, se a compra for parcelada, o programa deverá, primeiro, aplicar um juros de 50% sobre o valor inicial da compra e, depois, dividir o valor final (com juros) pela quantidade de parcelas recebida como entrada. Exiba, na tela, todo o resultado do processamento (valores inicial e final da compra, bem como a quantidade e o valor final da parcela) com duas casas decimais, quando possível.

valor = float(input("Digite o valor da compra: R$ "))
parcelas = int(input("Digite a quantidade de parcelas que deseja: "))

print("-" * 50)
print(f"O valor inicial da sua compra foi de R$ {valor:.2f}\nA quantidade de parcelas foi: {parcelas}")

if parcelas == 1:
  valor_final = valor - (valor * 0.1)
  print(f"O valor final da sua compra é de R$ {valor_final:.2f}, em parcela única.")
else:
  valor_final = valor + (valor * 0.5)
  valor_final_parcela = valor_final / parcelas
  print(f"O valor final da sua compra é de R$ {valor_final:.2f}\nO valor final de cada parcela é de R$ {valor_final_parcela:.2f}")