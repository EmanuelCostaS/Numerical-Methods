from funcoes import f, erro

erro_maximo = 0.01  # O erro máximo escolhido foi de 1% (0.01).
iteration_limit = 1000  # Definido um limite de iterações para evitar loop infinito.


def secant_method(x0, x1, iter_count=0):

    if iter_count >= iteration_limit:
        print("O método não convergiu dentro do limite de iterações.")
        return None

    f_x0 = f(x0)
    f_x1 = f(x1)

    if f_x1 == f_x0:  # Prevent division by zero
        print("Divisão por zero.")
        return None

    x2 = x1 - f_x1 * (x0 - x1) / (f_x0 - f_x1
                                  )  # Expressão do método das secantes.
    error = erro(x2, x1)  # Calcula o erro atual.

    print(f"Iteração {iter_count + 1}: x = {x2}, Erro = {100 * error}%")

    if error < erro_maximo:  # Caso o erro seja menor que 1%, o programa encerra e retorna a raiz encontrada.
        print(f"A raiz encontrada após {iter_count + 1} iterações foi: {x2}\n")
        return x2
    else:  # Caso o erro seja maior que 1%, o programa continua a execução recursivamente.
        return secant_method(x1, x2, iter_count + 1)
