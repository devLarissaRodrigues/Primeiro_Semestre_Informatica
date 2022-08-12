#Escreva uma função em Python capaz de retornar a soma apenas dos números pares de uma lista de números quaisquer fornecida como entrada para o programa. A função deve receber como parâmetros a lista e retornar o número representando a soma. Se nenhuma entrada for realizada (lista estiver vazia), a função deve retornar 0; Agora, escreva um programa que faça a leitura dos números como entrada do usuário, armazene-os em uma lista e, por fim, faça a chamada da função implementada.

def criar_lista():

  while True:
    numero = float(input("Digite um número ou 0 para parar: "))
    if numero == 0:
      break
    else:
      lista.append(numero)


def lista_pares():
  
  for i in range(len(lista)):
    if lista[i] % 2 == 0:
      lista_par.append(lista[i])


lista = []
lista_par = []

criar_lista()
lista_pares()


print(f"A lista dos números pares é {lista_par}")
print(f"A soma dos números pares da lista é {sum(lista_par)}")




