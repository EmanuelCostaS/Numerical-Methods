from pontoFixo import pontoFixo
from MetodoSecantes import secant_method
from NewtonRaphson import newton_raphson
from metodobissecao import bissecao

chute_inicial_PF = 0.8
chute_inicial_NR = 0.75
chute_inicial_Secantes1 = 0.75
chute_inicial_Secantes2 = 0.8
chute_inicial_Bisseccao1 = 0.75
chute_inicial_Bisseccao2 = 0.8

print("Método do Ponto fixo:\nChute inicial = 0.8")
pontoFixo(chute_inicial_PF)

print("Método de Newton-Raphson:\nChute inicial = 0.75")
newton_raphson(chute_inicial_NR)

print("Método das Secantes:\nChutes iniciais = 0.75 e 0.8")
secant_method(chute_inicial_Secantes1, chute_inicial_Secantes2)

print("Método da Bissecção:\nChutes iniciais = 0.75 e 0.8")
bissecao(chute_inicial_Bisseccao1, chute_inicial_Bisseccao2)

