from funcoes import f, f_linha, erro

erro_maximo = 1e-2  # O erro máximo escolhido foi de 1% (0.01).
iteration_limit = 1000  # Definido um limite de iterações para evitar loop infinito.

def newton_raphson(x0, iter_count=0):  # Adicionado iter_count para contar as iterações.
  if iter_count >= iteration_limit:
    print("O método não convergiu dentro do limite de iterações.")
    return None

  f_x0 = f(x0)  # Inicializa a variável f_x0 com o valor da função f(x0).
  df_x0 = f_linha(x0)  # Inicializa a variável df_x0 com o valor da derivada da função f(x0)

  x1 = x0 - (f_x0 / df_x0)  # Calcula a nova estimativa da raiz.
  error = erro(x0, x1)  # Calcula o erro inicial.

  print(f"Iteração {iter_count + 1}: x = {x1}, Erro = {100 * error}%")

  if error > erro_maximo:  # Se o erro calculado for maior que o erro máximo escolhido, então:
    return newton_raphson(x1, iter_count + 1)  # Chama a função recursivamente, passando o novo x0 como parâmetro.
  else:  # Se o erro calculado for menor ou igual ao erro máximo escolhido, então
    print(f'A raiz encontrada após {iter_count + 1} iterações foi: {x1}\n')
    return x1  # Retorna a raiz encontrada.