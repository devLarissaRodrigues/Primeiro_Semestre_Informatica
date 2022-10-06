#Uma empresa de mineração faz, periodicamente, um estudo sobre a produção de urânio em sua mina. Por causa do mau tempo, a mina produziu urânio apenas durante 1 semana. Escreva um algoritmo que leia a produção de urânio (em Kg) de cada dia da semana e armazene estas informações em uma lista. Ao final, calcule e exiba: (a) a produção média da minha; e (b) o dia (juntamente com o valor produzido) em que aconteceu a menor produção de urânio da empresa. Seu programa deve utilizar funções para realizar estes processamentos.

def lista_producoes():  
  producao_diaria.append(float(input(f"Digite a produção de minério de {dias_da_semana[cont]} (em kg): ")))
  return producao_diaria
  
dias_da_semana = ['segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo']
producao_diaria = []

def saida():
  print(f"\nA média de produção diária é de {sum(producao_diaria)/7:.2f} kg\nA menor produção da semana foi {min(producao_diaria)} kg, produzido {dias_da_semana[producao_diaria.index(min(producao_diaria))]}.")

for cont in range(7):
  lista_producoes()
saida()
