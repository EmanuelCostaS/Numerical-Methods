# Part 1: Gaussian Elimination and Iterative Methods in Python

## Gaussian Elimination

### Files:
- `EliminacaoGaussiana.py`

### Overview:
The Gaussian Elimination method is a direct approach for solving systems of linear equations. It involves two main steps:
1. **Forward Elimination** (`eliminacao_progressiva`): This process transforms the system's matrix into an upper triangular form.
2. **Backward Substitution** (`substituicao_regressiva`): Once in triangular form, the system is solved by substituting back the values from the last row upwards.

### Functions:
- **`eliminacao_progressiva(A, b)`**: 
    - Transforms the matrix `A` into an upper triangular matrix.
    - Adjusts the vector `b` accordingly during the process.
- **`substituicao_regressiva(A, b)`**:
    - Solves the upper triangular system obtained from the forward elimination step.
    - Outputs the solution vector `x`.
- **`EliminacaoGaussiana(A, b)`**:
    - A wrapper function that combines both forward elimination and backward substitution to solve the system.

### Usage:
```python
import numpy as np
from EliminacaoGaussiana import EliminacaoGaussiana

A = np.array([[0.3, 0.27, 0.15], 
              [0.25, 0.4, 0.2], 
              [0.15, 0.27, 0.3]], dtype=float)
b = np.array([200, 250, 180], dtype=float)

EliminacaoGaussiana(A, b)
```

---

## Iterative Methods - Jacobi and Gauss-Seidel

### Files:
- `metodoJacobi.py`
- `metodoGaussSeidel.py`
- `main.py`

### Overview:
The **Jacobi** and **Gauss-Seidel** methods are iterative approaches for solving systems of linear equations, often applied to large or sparse systems where direct methods like Gaussian Elimination are less efficient.

### Functions:
#### `metodoJacobi.py`:
- **`metodoJacobi(A, b, x, n, iter_max, tolerancia)`**:
    - An iterative method that updates all components of the solution vector `x` simultaneously using the values from the previous iteration.
    - Stops when the relative error is below a specified tolerance or the maximum number of iterations is reached.

#### `metodoGaussSeidel.py`:
- **`metodoGaussSeidel(A, b, x, n, iter_max, tolerancia)`**:
    - Similar to Jacobi, but the solution vector `x` is updated as soon as new values are computed, making it generally faster to converge.
    - Stops under the same conditions as Jacobi.

### Usage in `main.py`:
```python
import numpy as np
from metodoJacobi import metodoJacobi
from metodoGaussSeidel import metodoGaussSeidel
from EliminacaoGaussiana import EliminacaoGaussiana

# Define the system
A = np.array([[0.3, 0.27, 0.15], 
              [0.25, 0.4, 0.2], 
              [0.15, 0.27, 0.3]], dtype=float)
b = np.array([200, 250, 180], dtype=float)

# Initial guesses
x_zeros = np.zeros(len(b), dtype=float)
x_heuristico = np.array([230, 435, 95], dtype=float)

# Apply Jacobi Method
print("Método de Jacobi:")
print("Chute Inicial Zerado:", metodoJacobi(A, b, x_zeros, len(A), 1000, 0.01))
print("Chute Inicial Heurístico:", metodoJacobi(A, b, x_heuristico, len(A), 1000, 0.01))

# Apply Gauss-Seidel Method
print("Método de Gauss-Seidel:")
print("Chute Inicial Zerado:", metodoGaussSeidel(A, b, x_zeros, len(A), 1000, 0.01))
print("Chute Inicial Heurístico:", metodoGaussSeidel(A, b, x_heuristico, len(A), 1000, 0.01))

# Apply Gaussian Elimination
print("Eliminação de Gauss:")
EliminacaoGaussiana(A, b)
```

### Notes:
- **Convergence**: The convergence of Jacobi and Gauss-Seidel methods depends on the properties of matrix `A`. Diagonally dominant or symmetric positive definite matrices generally ensure convergence.
- **Accuracy**: The tolerance parameter should be chosen carefully to balance between accuracy and computation time.

---

# Part 2: Solving Systems of Linear Equations

This part of the repository contains Python implementations of methods to solve systems of linear equations using different numerical methods.

### Files

- **EliminacaoGaussiana.py**: This script contains the implementation of the Gaussian Elimination method for solving systems of linear equations. It includes functions for forward elimination and back substitution.
  
- **metodoJacobi.py**: This script implements the Jacobi method, an iterative algorithm to solve linear systems. The method converges to the solution by iteratively updating the estimates of the solution vector.
  
- **metodoGaussSeidel.py**: This script implements the Gauss-Seidel method, an iterative technique for solving linear systems. Unlike the Jacobi method, Gauss-Seidel updates the solution vector immediately after each step, potentially leading to faster convergence.

- **main.py**: This is the main script that ties together the Gaussian Elimination, Jacobi, and Gauss-Seidel methods. It defines a system of linear equations and solves it using the different methods, comparing the results with different initial guesses.

### Usage

1. **Gaussian Elimination**:
   ```python
   import numpy as np
   from EliminacaoGaussiana import EliminacaoGaussiana

   A = np.array([[...], [...], [...]])
   b = np.array([...])
   EliminacaoGaussiana(A, b)
   ```

2. **Jacobi Method**:
   ```python
   import numpy as np
   from metodoJacobi import metodoJacobi

   A = np.array([[...], [...], [...]])
   b = np.array([...])
   x_initial = np.zeros(len(b))
   metodoJacobi(A, b, x_initial, len(A), 1000, 0.01)
   ```

3. **Gauss-Seidel Method**:
   ```python
   import numpy as np
   from metodoGaussSeidel import metodoGaussSeidel

   A = np.array([[...], [...], [...]])
   b = np.array([...])
   x_initial = np.zeros(len(b))
   metodoGaussSeidel(A, b, x_initial, len(A), 1000, 0.01)
   ```

---

## Numerical Methods for Non-Linear Equations

This part of the repository contains Python implementations of various numerical methods for finding roots of non-linear equations.

### Overview:
Root-finding algorithms are used to determine where a given function crosses the x-axis (i.e., where `f(x) = 0`). These methods are essential for solving equations that cannot be solved algebraically.

### Files

- **funcoes.py**: Contains the functions required for the numerical methods, including the function `f(x)` whose root we want to find, its derivative `f_linha(x)`, and the fixed-point iteration function `g()`.
  
- **graphs.py**: This script generates graphs of the values and errors of different numerical methods (Fixed-Point, Newton-Raphson, Secant, and Bisection) across iterations.

- **main.py**: The main script that calls different root-finding methods using initial guesses and displays the results.
  
- **metodoBissecao.py**: Implements the Bisection method for finding roots of a function. This method repeatedly narrows down an interval where the root lies until the desired precision is achieved.
  
- **MetodoSecantes.py**: Implements the Secant method, which is a root-finding algorithm that uses a sequence of roots of secant lines to approximate the root.
  
- **NewtonRaphson.py**: Implements the Newton-Raphson method, which uses the derivative of the function to iteratively find a better approximation of the root.

- **pontoFixo.py**: Implements the Fixed-Point Iteration method for finding roots. The method involves iteratively applying a function `g(x)` until the output stabilizes.

### Usage

1. **Fixed-Point Method**:
   ```python
   from pontoFixo import pontoFixo

   chute_inicial = 0.8
   pontoFixo(chute_inicial)
   ```

2. **Newton-Raphson Method**:
   ```python
   from NewtonRaphson import newton_raphson

   chute_inicial = 0.75
   newton_raphson(chute_inicial)
   ```

3. **Secant Method**:
   ```python
   from MetodoSecantes import secant_method

   chute_inicial_1 = 0.75
   chute_inicial_2 = 0.8
   secant_method(chute_inicial_1, chute_inicial_2)
   ```

4. ** Bisection Method**:
   ```python
   from metodoBissecao import bissecao

   xl = 0.75
   xu = 0.8
   bissecao(xl, xu)
   ```

### Notes:
- **Convergence**: Each method has different convergence properties, which may depend on the function's nature and the choice of initial guesses.
- **Accuracy**: As with linear methods, tolerance parameters should be chosen carefully to balance accuracy and computational resources.
