#Segunda questão:

#Faça um programa para um restaurante capaz de efetuar o cálculo da conta. Para obter o cálculo, o usuário deverá fornecer ao programa: a) o nome do garçom, b) o número da mesa, c) o valor inicial da conta (sem 10% do garçom), e d) o número de integrantes da mesa. O programa, então, deverá apresentar estes valores digitados juntamente com o cálculo dos 10% do garçom, o novo valor final da despesa (com 10% do garçom) e, finalmente, quanto cada integrante da mesa deverá pagar. Exiba, na tela, o resultado do processamento com duas casas decimais, quando possível.

nome = input("Digite seu nome: ")
mesa = int(input("Digite o número da mesa: "))
conta = float(input("Digite o valor inicial da conta (sem 10% do garçom): "))
pessoas = int(input("Digite o número de integrantes da mesa: "))

percentual_garcom = conta * 0.1
conta_final = conta + percentual_garcom

valor_por_pessoa = conta_final/pessoas

print("-"*60)
print(f"DADOS: \nNome: {nome}\nMesa: {mesa}\nConta: R$ {conta:.2f}\nQuantidade de integrantes da mesa: {pessoas}")
print(f"O valor dos 10% do garçom corresponde a R$: {percentual_garcom:.2f}\nA conta final é de R$ {conta_final:.2f}\nO valor a ser pago por pessoa é de R$ {valor_por_pessoa:.2f}")
