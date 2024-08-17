from funcoes import f

def bissecao(xl, xu, tol=0.01, max_iter=1000):
    iter = 0  # Inicializar uma variável iter para contar o número de iterações

    while iter < max_iter:  # Enquanto não atingir o número máximo de iterações
        xr = (xl + xu) / 2 #Calcular o ponto médio xr
        fxr = f(xr)  #Calcular o valor da função no ponto médio

        print(f"Iteração {iter+1}: x = {xr}, Erro = {abs(fxr)}%")
        if abs(fxr) < tol: # Verificar se a tolerância foi satisfeita
            print(f"A raiz encontrada após {iter + 1} iterações foi:", xr)
            return xr #retorna xr como raiz aprox

        if f(xl) * fxr < 0: #Atualizar xu ou xl baseado no sinal de f(xl) * f(xr)
            xu = xr #está no intervalo inferior
        else:
            xl = xr #está no intervalo superior

        iter += 1  #Incrementar iter
    print("Não alcançou a precisão desejada dentro do nº máx de iterações")
    return xr