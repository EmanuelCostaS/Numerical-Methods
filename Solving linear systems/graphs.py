import matplotlib.pyplot as plt

# Dados fornecidos
metodos = {
    'Ponto Fixo': {
        'iteracoes': [1, 2],
        'valores': [0.8, 0.77827376143199],
        'erros': [2.7915933498817562, 0.0]
    },
    'Newton-Raphson': {
        'iteracoes': [1, 2, 3, 4],
        'valores': [0.8181791533004505, 0.7932492109875091, 0.7788981258105961, 0.7781060744999247],
        'erros': [8.333034766948394, 3.142762951116757, 1.842485519139984, 0.10179220245522835]
    },
    'Secantes': {
        'iteracoes': [1, 2],
        'valores': [0.7668325370749522, 0.7739358185360022],
        'erros': [4.145932865630975, 0.9263145625178003]
    },
    'Bissecção': {
        'iteracoes': [1, 2, 3, 4],
        'valores': [0.775, 0.7875000000000001, 0.78125, 0.778125],
        'erros': [0.011830924399521395, 0.04259743429925186, 0.012127980295575616, 0.000570525639478528]
    }
}

# Gráfico de Valores
plt.figure(figsize=(10, 6))
for metodo, dados in metodos.items():
    plt.plot(dados['iteracoes'], dados['valores'], marker='o', label=f'{metodo}')

plt.xlabel('Iterações')
plt.ylabel('Valores')
plt.title('Valores por Iteração')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Erros
plt.figure(figsize=(10, 6))
for metodo, dados in metodos.items():
    plt.plot(dados['iteracoes'], dados['erros'], marker='x', linestyle='--', label=f'{metodo}')

plt.xlabel('Iterações')
plt.ylabel('Erros (%)')
plt.title('Erros por Iteração')
plt.legend()
plt.grid(True)
plt.show()
