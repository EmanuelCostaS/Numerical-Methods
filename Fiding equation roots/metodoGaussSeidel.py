import numpy as np

def metodoGaussSeidel(A, b, x, n, iter_max, tolerancia):
  iter_inicial = 0
  x_antigo = x.copy()  # Faz uma cópia do vetor x

  while iter_inicial < iter_max:
      for i in range(n):
          soma = 0
          for j in range(n):
              if j < i:
                  soma += A[i][j] * x[j]
              elif j > i:
                  soma += A[i][j] * x_antigo[j]
          x[i] = (b[i] - soma) / A[i][i]

      # Verifica o erro relativo
      erro_relativo = np.linalg.norm(x - x_antigo) / np.linalg.norm(x)
      if erro_relativo < tolerancia:
          
          return x

      x_antigo = x.copy()  # Faz uma cópia do vetor x atualizado
      iter_inicial += 1
    

  return x