import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ano = 365*24 # Quantidade de horas em um ano
    r = 0.0003  # Taxa de decaimento

    t = np.linspace(0, 3 * ano, 1000)
    Q = np.zeros_like(t)

    ind1 = t <= ano
    Q[ind1] = 10000 * (1 - np.exp(-r * t[ind1]))

    ind2 = t > ano
    Q1 = 10000 * (1 - np.exp(-r * ano))
    Q[ind2] = Q1 * np.exp(-r * (t[ind2] - ano))

    plt.figure(figsize=(10,6))
    plt.plot(t / ano, Q, "b--", label="Quantidade de Químico Q(t)")

    plt.axvline(x=1, color='red', linestyle='--', label='Fim do Ano 1')

    plt.title("Quantidade de Produto Químico na lagoa em 3 anos")
    plt.xlabel("Tempo (anos)")
    plt.ylabel("Quantidade (gramas)")
    plt.grid(True)
    plt.legend()

    plt.show()