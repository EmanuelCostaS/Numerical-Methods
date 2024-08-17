import numpy as np
from metodoJacobi import metodoJacobi
from metodoGaussSeidel import metodoGaussSeidel
from EliminacaoGaussiana import EliminacaoGaussiana

# Matriz A e vetor b
A = np.array([[0.3, 0.27, 0.15], 
              [0.25, 0.4, 0.2], 
              [0.15, 0.27, 0.3]], dtype=float)
b = np.array([200, 250, 180], dtype=float)

# Chutes iniciais diferentes
x_zeros = np.zeros(len(b), dtype=float)
x_heuristico = np.array([230, 435, 95], dtype=float)

#print(x_media)

# Executando o Método de Jacobi com diferentes chutes iniciais

print("Método de Jacobi:")
print("Chute Inicial Zerado:", metodoJacobi(A, b, x_zeros, len(A), 1000, 0.01))
print("Chute Inicial Heurístico:", metodoJacobi(A, b, x_heuristico, len(A), 1000, 0.01))
print("")
print("Método de Gauss-Seidel:")
print("Chute Inicial Zerado:", metodoGaussSeidel(A, b, x_zeros, len(A), 1000, 0.01))
print("Chute Inicial Heurístico:", metodoGaussSeidel(A, b, x_heuristico, len(A), 1000, 0.01))
print("")
print("Eliminação de Gauss:")
EliminacaoGaussiana(A, b)
