# Assuma que seu programa possui a seguinte lista de nomes de clientes da empresa:
# clientes = ['caio', 'wellington', 'pedro', 'bruno', 'ana', 'caio', 'bruno', 'david', 'pedro']

clientes = ['caio', 'wellington', 'pedro', 'bruno', 'ana', 'caio', 'bruno', 'david', 'pedro']

nome = input("Digite um nome: ")

#Verificar se um dado nome passado como entrada se encontra na lista e informar o número de ocorrências:

print(f"\nO nome {nome} aparece na lista {clientes.count(nome)} vez(es)")

# Retornar a posição da primeira ocorrência de um dado nome na lista. Se o nome não existir, deve-se retornar o valor -1 sinalizando posição inválida não encontrada

if nome in clientes:
  print(f"O índice que o nome {nome} aparece na primeira ocorrência é o {clientes.index(nome)}")
else:
  print("-1")
  
# Retornar a posição da última ocorrência de um dado nome na lista. Se o nome não existir, deve-se retornar o valor -1 sinalizando posição inválida não encontrada

posicao = -1
for i in range(len(clientes)):
  if clientes[i] == nome:
    posicao = i

print(f"A posição de última ocorrência é {posicao}")
# Remover todas as ocorrências do nome de entrada presente na lista

contador = 0
for k in clientes:
  if k == nome:
    clientes.pop(contador)
  contador += 1
  
print(f"\nLista sem a ocorrência do nome {nome}: \n{clientes}")