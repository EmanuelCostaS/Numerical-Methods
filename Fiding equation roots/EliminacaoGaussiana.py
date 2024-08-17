import numpy as np

def eliminacao_progressiva(A, b):
  n = len(A) # Comprimento da matriz A

  for k in range(0, n): # Percorre os pivôs
    for i in range(k+1, n): # Percorre as linhas abaixo do pivô
      fator = A[i][k] / A[k][k] # Pivô

      for j in range(k, n): # Percorre as colunas depois do pivô
        A[i][j] = A[i][j] - fator * A[k][j] # Subtrai a linha pela abaixo do pivô multiplica-o
      b[i] = b[i] - fator * b[k] # Subtrai o elemento pelo abaixo do pivô multiplica-o

  return A, b

def substituicao_regressiva(A, b):
  n = len(A) # Comprimento da matriz A
  x = np.zeros(n) # Cria matriz para os resultados
  x[n - 1] = b[n - 1] / A[n - 1][n - 1] # Primeiro passo da substituição regressiva

  for i in range(n - 1, -1, -1): # Percorre as linhas de baixo pra cima, com excessão da última 
    soma = b[i]
    for j in range(i + 1, n): # Percorre as colunas depois do pivô
      soma = soma - A[i][j] * x[j] # Subtrai o elemento pelo abaixo do pivô multiplica-o
    x[i] = soma / A[i][i]

  print(x)
  return x

def EliminacaoGaussiana(A, b):

  A = A.astype(float)
  b = b.astype(float)

  eliminacao_progressiva(A, b)
  substituicao_regressiva(A, b)
  return A, b