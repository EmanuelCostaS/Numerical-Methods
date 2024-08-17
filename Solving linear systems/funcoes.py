import math

Ib = 0.1
Is = 10**-14
Vt = 0.026
erro_maximo = 0.01  # O erro máximo escolhido foi de 1% (0.01).
iteration_limit = 1000  # Definido um limite de iterações para evitar loop infinito.
tolerance = 1e-6

def f(x):
  try:
      exp_value = min(x / Vt, 700)  # Limita x/Vt para evitar Overflow
      return Is * (math.exp(exp_value) - 1) - Ib
  except OverflowError:
      return float('inf')

def f_linha(x):
  try:
      exp_value = min(x / Vt, 700)  # Limita x/Vt para evitar Overflow
      return Is * exp_value * math.exp(exp_value)
  except OverflowError:
      return float('inf')

def g():
    try:
        return Vt * math.log((Ib / Is) + 1)
    except ValueError:
        return float('inf')

def erro(x0, x1):  # Função que calcula o erro.
  return math.fabs((x1 - x0) / x1)