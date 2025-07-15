# Equação v(t) = 49 + Ce^{-t/5}.
# Para uma determinada velocidade desejada, foi encontrado um respectivo tempo. A questão desse cálculo é encontrar o espaço percorrido até esse tempo
# Para isso, foi feito a integral de 0 até 19.56 (tempo necessário para atingir a velocidade desejada) da função v(t)

# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Simplificando a expressão para v(t) = 49 * (1 - e^{-t/5}
def velocidade(t):
    return 49 * (1 - np.exp(-t / 5))

# Integrando v(t) chegamos a 49 * (t + 5 * e^(-t / 5)) + C, intervalos indo de 0 a 19.56. Para o primeiro intervalo (0), C = -245
def distancia(t):
    return 49 * (t + 5 * np.exp(-t / 5)) - 245

def plotar():
    tempoFinal = -5 * np.log(0.02)
    distanciaPercorrida = distancia(tempoFinal)

    print(f"Tempo para atingir 98% da vel. limite: {tempoFinal:.2f} segundos")
    print(f"Distância percorrida nesse tempo: {distanciaPercorrida:.2f} metros")

    tArray = np.linspace(0, tempoFinal, 500)
    vArray = velocidade(tArray)
    xArray = distancia(tArray)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.suptitle("Análise do Objeto em Queda", fontsize = 20)

    # Plot da Velocidade
    ax1.plot(tArray, vArray, label='Velocidade v(t)', color='blue')
    ax1.set_title('Velocidade vs. Tempo')
    ax1.set_xlabel('Tempo (s)')
    ax1.set_ylabel('Velocidade (m/s)')
    ax1.grid(True)
    ax1.legend()

    # Plot da Distância
    ax2.plot(tArray, xArray, label='Distância x(t)', color='purple')
    ax2.set_title('Distância vs. Tempo')
    ax2.set_xlabel('Tempo (s)')
    ax2.set_ylabel('Distância (m)')
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

if __name__ == '__main__':
    plotar()