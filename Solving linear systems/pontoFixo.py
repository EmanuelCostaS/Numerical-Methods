import math
from funcoes import g

iteration_limit = 1000  # Definido um limite de iterações para evitar loop infinito.
tolerance = 1e-2

def erro(x0, x1):  # Função que calcula o erro.
  return math.fabs((x1 - x0) / x1)

def pontoFixo(x0):
  iter = 0  # Número de iterações inicializado em zero.

  while iter < iteration_limit:
      x1 = g()
      err = float(erro(x0, x1))

      print(f"Iteração {iter + 1}: x = {x0}, Erro = {100 * err}%")

      if err < tolerance:
          print(f"A raiz encontrada após {iter + 1} iterações foi: {x1}\n")
          return x1

      x0 = x1  # Atualiza o valor de x0 para o valor de x1.
      iter += 1  # Incrementa o número de iterações.

  print("O método não convergiu dentro do limite de iterações.")
  return None