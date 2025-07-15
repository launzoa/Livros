import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

t = np.arange(0, 20, 0.1) # Intervalo de Tempo

vLinear = 49*(1-np.exp(-t/5)) # Resistência Linear
vQuad = 49*np.tanh(t/5) # Resistência Quadrática

plt.plot(t, vLinear, color="aqua", label="Reistência Linear")
plt.plot(t, vQuad, color="red", label="Resistência Quadrática")

plt.title("Comparação dos modelos de resistência do ar")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid(True) # Grade para leitura
plt.legend()

plt.show()

# Resolvendo a questão que pede para encontrar o tempo que leva para o objeto percorrer 300m.
# Pegamos a equação geral e igualamos igual a 0, ou seja, 300 = 245*log(cosh(t/5)) -> 245*log(cosh(t/5)) - 300
def equacaoGeral(time):
    equacao = 245 * np.log(np.cosh(time / 5))
    return equacao - 300

# Integramos a expressão e chegamos a 300 = 245*log(cosh(t/5)) -> log(cosh(t/5)) = 300/245 -> cosh(t/5) = e^(300/245)
# cosh(x) = (e^x + e^-x)/2 -> cosh(t/5) = (e^t/5 + e^-t/5) / 2 -> (e^t/5 + e^-t/5) / 2 = e^(60/49)
def equacaoIntegrada(time):
    equacao = (np.exp(time/5) + np.exp(-time/5)) / 2
    return equacao - np.exp(60/49)

# fsolve funciona com palpites, então quando sugerimos "10", ele tenta encontrar a condição que definimos na função, ou seja, equação - valor
# e em caso afirmativo, ou seja, caso essa diferença for 0 ele retorna o valor obtido para essa condição. Em caso negativo, ele faz testes com base em outros palites
# como por exemplo. f(3) = 3² - 25 = -16, ele vai falar "Estou longe... A inclinação é positiva, preciso aumentar o valor de x" e vai testar f(6)... até encontrar f(5)
tempoSolucaoGeral = fsolve(equacaoGeral, 10)
tempoSolucaoIntegral = fsolve(equacaoIntegrada, 10)

print("Usando a forma geral")
print("Tempo necessário para percorrer 300 metros: ", tempoSolucaoGeral[0])
print("Distancia percorrida: ", 245 * np.log(np.cosh(tempoSolucaoGeral[0] / 5)))

print("Usando a forma Integrada")
print("Tempo necessário para percorrer 300 metros: ", tempoSolucaoIntegral[0])
print("Distancia percorrida: ", 245 * np.log(np.cosh(tempoSolucaoIntegral[0] / 5)))